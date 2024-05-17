# Code Documentation

This code is a script written in Python to fetch repository details from GitHub, specifically the contents of files in a repository. It utilizes the Streamlit library for displaying the fetched files.

### Importing Libraries
- `requests`: Used for making HTTP requests to the GitHub API.
- `base64`: Used for decoding base64 encoded content fetched from the GitHub API.
- `streamlit as st`: Used for creating interactive web apps for displaying the fetched files.

### `GitHubRepoFetcher` Class
- `__init__(self, owner, repo)`: Constructor method to initialize the class with owner and repo details.
- `_fetch_contents(self, file_path="")`: Private method to recursively fetch the contents of files in the repository.
- `_fetch_file_content(self, file_path)`: Private method to fetch and decode the content of a specific file in the repository.
- `fetch_files(self)`: Public method to initiate the recursive fetching of files from the repository and return the fetched contents.
- `display_files(self)`: Public method to display the fetched files in Streamlit and print to the console.

### `Main` Class
- `main()`: Static method serving as the main execution point for the script.
- Initiates the `GitHubRepoFetcher` class with repository details.
- Fetches files from the repository using `fetch_files()` method.
- Displays the fetched files using Streamlit and prints to the console.

### Execution
- The script runs the `main()` method when executed.
- It specifies the repository details (owner and repo).
- Fetches and displays the files from the repository using Streamlit for visualization.

### Note
- The script uses Streamlit for displaying files in an interactive web app format.
- It utilizes recursive fetching to handle directories and their contents.
- Base64 encoding is used to decode content fetched from the GitHub API.