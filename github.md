# Code Documentation

## GitHubRepoFetcher Class
- The `GitHubRepoFetcher` class is responsible for fetching and storing file contents from a GitHub repository.
- Constructor:
    - `__init__(self, owner, repo)`: Initializes the class with owner and repo details.
- Methods:
    - `_fetch_contents(self, file_path="")`: Fetches contents of files recursively.
    - `_fetch_file_content(self, file_path)`: Fetches and decodes content of a specific file.
    - `fetch_files(self)`: Initiates fetching of files.
    - `display_files(self)`: Displays the fetched files in Streamlit and prints to the console.

## Main Class
- The `Main` class serves as the main execution point for the script.
- Methods:
    - `main()`: Main execution point for the script.

## Main Execution
- The script instantiates the `GitHubRepoFetcher` class with repository details, fetches files, and displays them using Streamlit.

## Import Statements
- `import requests`: Used for making HTTP requests.
- `import base64`: Used for encoding and decoding content.
- `import streamlit as st`: Used for creating interactive web apps.

## GitHub API
- The code interacts with the GitHub API to fetch file contents.

## Streamlit
- The fetched files are displayed using Streamlit for a user-friendly interface.

## Exception Handling
- The code includes error handling for failed API requests.

## Execution
- The `Main.main()` method is called to initiate the script execution.