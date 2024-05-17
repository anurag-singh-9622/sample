# Code Documentation

This code is designed to fetch repository information from GitHub and display the contents of the files in the repository using Streamlit.

## GitHubRepoFetcher Class

### Constructor
- `__init__(self, owner, repo)`: Initializes the GitHubRepoFetcher class with owner and repo details.

### Methods
- `_fetch_contents(self, file_path="")`: Fetches the contents of files in the repository recursively.
- `_fetch_file_content(self, file_path)`: Fetches and decodes the content of a specific file in the repository.
- `fetch_files(self)`: Initiates the recursive fetching of files from the repository.
- `display_files(self)`: Displays the fetched files in Streamlit and prints to the console.

## Main Class

### Static Method
- `main()`: Main execution point for the script.

## Execution
- The script specifies the repository details (owner and repo).
- Instantiates the GitHubRepoFetcher class with the specified details.
- Fetches files from the repository and displays them using Streamlit.

---

This code uses the `requests` library to interact with the GitHub API, `base64` for decoding file content, and `streamlit` for displaying the fetched files. The script provides a structured way to fetch and display the repository contents.