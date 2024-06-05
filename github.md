# Code Documentation

### GitHubRepoFetcher Class:
- **Attributes:**
  - owner: Owner of the GitHub repository
  - repo: Name of the GitHub repository
  - list_of_contents: Dictionary to store file contents
  - list_all_files: List to store all file paths

- **Methods:**
  - **\_\_init\_\_(self, owner, repo):**
    - Constructor method to initialize the class attributes.
  
  - **\_fetch_contents(self, file_path=""):**
    - Fetches the contents of files in the repository recursively.
  
  - **\_fetch_file_content(self, file_path):**
    - Fetches and decodes the content of a specific file in the repository.
  
  - **fetch_files(self):**
    - Initiates the recursive fetching of files from the repository.
  
  - **display_files(self):**
    - Displays the fetched files in Streamlit and prints to the console.

### Main Class:
- **Methods:**
  - **main():**
    - Main execution point for the script.
    - Specifies the repository details.
    - Instantiates the GitHubRepoFetcher class.
    - Fetches files from the repository.
    - Displays the fetched files using Streamlit and prints to the console.

### Execution:
- The script fetches and displays files from a specified GitHub repository using the GitHubRepoFetcher class.
- The Main class is the entry point for executing the script.
- The code uses the Streamlit library for displaying the fetched files.