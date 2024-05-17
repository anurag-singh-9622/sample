# Code Documentation

### Introduction
This code is designed to fetch repository information from GitHub, specifically fetching and displaying the contents of files in a repository.

### Importing Libraries
- `requests`: Used to make HTTP requests to the GitHub API.
- `base64`: Used to decode Base64 encoded content.
- `streamlit as st`: Used for displaying the fetched files in a Streamlit app.

### `GitHubRepoFetcher` Class
- `__init__(self, owner, repo)`: Constructor method that initializes the class with owner and repo details, along with empty dictionaries/lists to store file contents and paths.
- `_fetch_contents(self, file_path="")`: Private method to recursively fetch the contents of files in the repository.
- `_fetch_file_content(self, file_path)`: Private method to fetch and decode the content of a specific file.
- `fetch_files(self)`: Method to initiate the recursive fetching of files from the repository and return the list of contents.
- `display_files(self)`: Method to display the fetched files in Streamlit and print to the console.

### `Main` Class
- `main()`: Static method that serves as the main execution point for the script.
- The owner and repo details are specified.
- An instance of `GitHubRepoFetcher` is created with the specified owner and repo.
- Files are fetched from the repository using the `fetch_files` method.
- Fetched files are displayed using the `display_files` method.

### Execution
- The `Main.main()` method is called if the script is run directly.

### Note
- This code fetches and displays the contents of files in a GitHub repository using the GitHub API and Streamlit for visualization.