# Code Documentation

This code is a Python script that fetches and displays the contents of files in a GitHub repository. It uses the `requests` library to make API calls to GitHub and `streamlit` for displaying the fetched files.

## GitHubRepoFetcher Class

### Constructor
- `__init__(self, owner, repo)`: Initializes the GitHubRepoFetcher class with the owner and repository name.
- `owner`: Owner of the GitHub repository.
- `repo`: Name of the GitHub repository.
- `list_of_contents`: Dictionary to store file contents.
- `list_all_files`: List to store all file paths.

### Methods
- `_fetch_contents(self, file_path="")`: Fetches the contents of files in the repository recursively.
- `_fetch_file_content(self, file_path)`: Fetches and decodes the content of a specific file in the repository.
- `fetch_files(self)`: Initiates the recursive fetching of files from the repository.
- `display_files(self)`: Displays the fetched files in Streamlit and prints to the console.

## Main Class

### Static Method
- `main()`: Main execution point for the script.

### Execution
- Specify the repository details (owner and repo).
- Instantiate the `GitHubRepoFetcher` class with the owner and repo.
- Fetch files from the repository using `fetch_files` method.
- Display the fetched files using `display_files` method.

## Execution
- The script fetches files from a specified GitHub repository and displays them using Streamlit.
- The main function `Main.main()` is called to execute the script.