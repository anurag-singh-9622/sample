### Imports
- `requests`: Used for making HTTP requests.
- `base64`: Used for encoding and decoding data.
- `streamlit as st`: Used for creating interactive web apps.

### Variables
- `owner`: Represents the owner of the GitHub repository.
- `repo`: Represents the name of the repository.
- `list_of_contents`: Dictionary to store the contents of fetched files.
- `list_all_files`: List to store all file paths.

### Functions
- `_fetch_contents`: Recursively fetches the contents of files in the repository.
- `_fetch_file_content`: Fetches and decodes the content of a specific file in the repository.
- `fetch_files`: Initiates the recursive fetching of files from the repository.
- `display_files`: Displays the fetched files in Streamlit and prints to the console.
- `main`: Main execution point for the script.

### Function Parameters
- `self`: Refers to the instance of the class.
- `owner`: Represents the owner of the GitHub repository.
- `repo`: Represents the name of the repository.
- `file_path`: Path of the file to fetch.

### Classes
- `GitHubRepoFetcher`: Class to fetch files from a GitHub repository.
- `Main`: Class representing the main execution point for the script.

### Class Attributes
- `owner`: Owner of the repository.
- `repo`: Repository name.
- `list_of_contents`: Dictionary to store file contents.
- `list_all_files`: List to store all file paths.

### Class Methods
- `_fetch_contents`: Fetches contents of files recursively.
- `_fetch_file_content`: Fetches and decodes file content.
- `fetch_files`: Initiates the fetching of files from the repository.
- `display_files`: Displays fetched files.

### IF/Else
- Used for handling different status codes returned by the API calls.

### Algorithm Used
- The script recursively fetches files from a GitHub repository using the GitHub API and decodes file contents.

### Data Structures
- Dictionary and lists are used to store file contents and paths.

### Suggestions
1. It's recommended to handle exceptions more gracefully by providing detailed error messages or logging errors.
2. Avoid using print statements directly in methods. Consider using a logging mechanism for better error handling and debugging.
3. Encapsulate the Streamlit display logic in a separate function/class for better organization.
4. Add comments to explain complex logic or important sections of the code for better readability.