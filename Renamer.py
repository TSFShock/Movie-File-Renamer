import os
import re
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# API key for themoviedb.org
API_KEY = "API_KEY"
BASE_URL = "https://api.themoviedb.org/3/search/movie"

def get_movie_info(movie_title, release_year):
    params = {
        'api_key': API_KEY,
        'query': movie_title,
        'year': release_year  # Include release year in the query
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data['results']:
        return data['results'][0]  # Return the first result
    else:
        return None

def extract_info_from_filename(file_name):
    # Extract movie title, chapter number, and year from the file name
    match = re.match(r'^(.+)\.chapter\.\d+\.(20\d{2})\.', file_name)
    if match:
        movie_title = match.group(1).replace('.', ' ')  # Replace dots with spaces
        release_year = match.group(2)
        return movie_title, release_year
    else:
        return None, None

def clean_title(title):
    # Remove common separators and additional text
    title = re.sub(r'[-._]', ' ', title)
    # Remove characters not allowed in Windows file names
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Remove leading and trailing whitespace
    title = title.strip()
    return title

def rename_movie(file_path, new_title, release_year):
    file_dir, file_name = os.path.split(file_path)
    file_ext = os.path.splitext(file_name)[1]
    new_title_cleaned = re.sub(r'[<>:"/\\|?*]', '', new_title)
    new_title_cleaned = new_title_cleaned.replace(':', '-')  # Replace colon with hyphen
    new_file_name = os.path.join(file_dir, f"{new_title_cleaned} ({release_year}){file_ext}")
    try:
        os.rename(file_path, new_file_name)
        print(f"File renamed to: {new_file_name}")
    except OSError as e:
        print(f"Error renaming file: {e}")

def main():
    # Ask user to select a file
    Tk().withdraw()
    file_path = askopenfilename(title="Select a movie file", filetypes=[("Video Files", "*.mkv *.mp4 *.avi")])
    
    if not file_path:
        print("No file selected.")
        return
    
    # Extract movie title and release year from file name
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    movie_title, release_year = extract_info_from_filename(file_name)
    
    if movie_title and release_year:
        print(f"Extracted movie title: {movie_title}")
        print(f"Release year: {release_year}")
        
        # Clean the title before querying the API
        cleaned_title = clean_title(movie_title)
        print(f"Cleaned movie title: {cleaned_title}")
        
        # Fetch movie information
        movie_info = get_movie_info(cleaned_title, release_year)
        
        if movie_info:
            print("Found movie information:")
            print(f"Title: {movie_info['title']}")
            print(f"Overview: {movie_info['overview']}")
            print(f"Release Date: {movie_info['release_date']}")
            print(f"Original Title: {movie_info['original_title']}")
            print(f"Vote Average: {movie_info['vote_average']}")
            print(f"Vote Count: {movie_info['vote_count']}")
            print(f"Popularity: {movie_info['popularity']}")
            
            confirm_rename = input("Do you want to rename the file? (yes/no): ")
            if confirm_rename.lower() == 'yes':
                new_title = movie_info['title']
                rename_movie(file_path, new_title, release_year)
            else:
                print("File not renamed.")
        else:
            print("Movie information not found.")
    else:
        print("Unable to extract movie information from file name.")

if __name__ == "__main__":
    main()
