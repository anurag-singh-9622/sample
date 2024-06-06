# Code Documentation

### Importing Required Modules
- Importing the Document class from the docx module to work with Word documents.
- Importing BeautifulSoup for parsing HTML content.

### HTML Content
- A sample HTML content is stored in a variable.
- It includes a title, styling for 'h1' and 'p' tags, and some sample text.

### Creating a New Word Document
- An instance of the Document class is created to work with the Word document.

### Parsing HTML Content
- The HTML content is parsed using BeautifulSoup with the 'html.parser'.

### Extracting and Formatting Text
- Iterate through 'h1' and 'p' tags in the HTML content.
- If the tag is 'h1', add a heading with the text.
- If the tag is 'p', add a paragraph with the text.

### Saving Document
- Store the created document in a variable for further use.

### Printing for Demonstration
- Print the text of the first paragraph in the document for demonstration purposes.