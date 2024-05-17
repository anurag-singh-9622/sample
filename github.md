# Code Documentation

This code is used to fetch repository details from GitHub and display the files in Streamlit.

## GitHubRepoFetcher Class
- `__init__(self, owner, repo)`: Constructor method to initialize the owner and repository details, along with empty dictionaries and lists.
- `_fetch_contents(self, file_path="")`: Method to fetch the contents of files in the repository recursively.
- `_fetch_file_content(self, file_path)`: Method to fetch and decode the content of a specific file in the repository.
- `fetch_files(self)`: Method to initiate the recursive fetching of files from the repository.
- `display_files(self)`: Method to display the fetched files in Streamlit and print to the console.

## Main Class
- `main()`: Static method that serves as the main execution point for the script.

## Execution
- The `Main.main()` function is called when the script is run.
- It specifies the owner and repository details.
- Instantiates the `GitHubRepoFetcher` class with the owner and repository.
- Fetches files from the repository using the `fetch_files()` method.
- Displays the fetched files in Streamlit and prints them to the console.

## Libraries Used
- `requests`: To make HTTP requests to the GitHub API.
- `base64`: To decode the content of files fetched from GitHub.
- `streamlit`: To create interactive web apps for displaying the fetched files.

This code provides a structured way to fetch and display repository details from GitHub using Python and Streamlit.