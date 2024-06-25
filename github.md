# Code Documentation

### Introduction
This code is designed to fetch and display files from a GitHub repository using the GitHub API. It utilizes the `requests` library to make API calls, `base64` for decoding file content, and `streamlit` for displaying the files in a user-friendly interface.

### GitHubRepoFetcher Class
- #### `__init__(self, owner, repo)`
  - Constructor method that initializes the `GitHubRepoFetcher` object with the specified owner and repository.
  - `list_of_contents`: Dictionary to store file contents.
  - `list_all_files`: List to store all file paths.

- #### `_fetch_contents(self, file_path="")`
  - Fetches the contents of files in the repository recursively.
  - Uses the GitHub API to retrieve file information.
  - Recursively called for directories to fetch files.
  
- #### `_fetch_file_content(self, file_path)`
  - Fetches and decodes the content of a specific file in the repository.
  - Decodes the base64 content to human-readable text.

- #### `fetch_files(self)`
  - Initiates the recursive fetching of files from the repository.
  - Returns the dictionary of file contents.

- #### `display_files(self)`
  - Displays the fetched files in Streamlit and prints to the console.
  - Uses Streamlit to showcase each file's content.

### Main Class
- #### `main()`
  - Main execution point for the script.
  - Specifies the owner and repository details.
  - Instantiates the `GitHubRepoFetcher` class.
  - Fetches and displays files from the repository.

### Execution
- Executes the `Main.main()` method to start fetching and displaying files from the specified GitHub repository.