# Code Documentation

This code fetches repository details from GitHub and displays the files in Streamlit.

### GitHubRepoFetcher Class
- **Attributes**:
  - `owner`: Owner of the repository
  - `repo`: Name of the repository
  - `list_of_contents`: Dictionary to store file contents
  - `list_all_files`: List to store all file paths

- **Methods**:
  - `_fetch_contents(self, file_path="")`: Fetches contents of files in the repository recursively.
  - `_fetch_file_content(self, file_path)`: Fetches and decodes content of a specific file.
  - `fetch_files(self)`: Initiates recursive fetching of files.
  - `display_files(self)`: Displays fetched files in Streamlit and prints to console.

### Main Class
- **Methods**:
  - `main()`: Main execution point for the script.

### Execution Flow
1. Instantiate `GitHubRepoFetcher` with owner and repo details.
2. Fetch files from the repository.
3. Display the fetched files using Streamlit.

### Usage
1. Run the script.
2. Specify the repository details.
3. Files and their contents will be displayed in Streamlit and printed to the console.