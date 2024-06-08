# Movie File Renamer

This Python script allows you to rename movie files based on their metadata fetched from themoviedb.org API. It extracts information such as the movie title, release year, overview, original title, vote average, and popularity. You can use this script to organize your movie library by ensuring accurate and standardized file names.

## How to Use

1. **API Key**: Before running the script, make sure to replace `API_KEY` with your own API key from themoviedb.org. You can sign up for an account and get your API key [here](https://www.themoviedb.org/settings/api).

2. **Dependencies**: Install the required dependencies using `pip install -r requirements.txt`. The script uses `requests` for API requests and `tkinter` for the file dialog.

3. **Select a File**: When you run the script, it will prompt you to select a movie file (supports `.mkv`, `.mp4`, and `.avi` formats).

4. **Extract Information**: The script will extract the movie title and release year from the file name. It will then clean the title for querying the API.

5. **Fetch Movie Information**: The cleaned movie title and release year are used to fetch movie information from themoviedb.org API. If the information is found, it will display details like title, overview, release date, etc.

6. **Rename File**: You have the option to rename the file using the fetched movie title and release year. Confirm the rename when prompted.

## Example File Name Format

The script expects the file name to follow a specific format for extracting information:

```
{Movie Title}.chapter.{Chapter Number}.{Release Year}.ext
```

For example:

```
Inception.chapter.1.2010.mkv
```

## Note

- Ensure your internet connection is active to fetch movie information from the API.
- The script automatically cleans the title for Windows file name compatibility.
- Renaming a file will modify its name and extension.

Feel free to contribute, report issues, or suggest improvements. Happy organizing your movie collection!
