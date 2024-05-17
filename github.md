# Code Documentation

This code fetches the repository information from GitHub and displays the fetched files using Streamlit. Below is a detailed explanation of each part of the code:

## GitHubRepoFetcher Class
- `__init__(self, owner, repo)`: Initializes the class with the owner and repository name. It also initializes two attributes to store file contents and paths.
- `_fetch_contents(self, file_path="")`: Fetches the contents of files in the repository recursively. It makes API requests to GitHub and stores the file contents in a dictionary.
- `_fetch_file_content(self, file_path)`: Fetches and decodes the content of a specific file in the repository using base64 decoding.
- `fetch_files(self)`: Initiates the recursive fetching of files from the repository and returns the list of contents.
- `display_files(self)`: Displays the fetched files using Streamlit and prints them to the console.

## Main Class
- `main()`: Main execution point for the script. It specifies the repository details, instantiates the `GitHubRepoFetcher` class, fetches files from the repository, and displays the fetched files.

## Usage
- To use this script, set the `owner` and `repo` variables with the GitHub repository owner and name.
- Run the script to fetch and display the files from the specified repository.

This code provides a structured way to fetch and display repository files, making it easy for beginners to understand and use.