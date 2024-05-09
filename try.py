```python
from docx import Document  # Importing the Document class from the docx module
from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML content

# HTML content (replace with your actual HTML)
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sample HTML</title>
    <style>
        h1 { color: blue; }
        p { font-size: 14px; }
    </style>
</head>
<body>
    <h1>Hello, Markdown!</h1>
    <p>This is a sample paragraph.</p>
</body>
</html>
'''

# Create a new Word document
doc = Document()  # creating an instance of the Document class

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')  # parsing the HTML content using BeautifulSoup

# Extract and add text and formatting to the document
for tag in soup.find_all(['h1', 'p']):  # iterating through 'h1' and 'p' tags in the HTML content
    if tag.name == 'h1':  # checking if the tag is 'h1'
        doc.add_heading(tag.text, level=1)  # adding a heading with the text from the 'h1' tag
    elif tag.name == 'p':  # checking if the tag is 'p'
        doc.add_paragraph(tag.text)  # adding a paragraph with the text from the 'p' tag

# Save the document in memory (in a variable)
docx_output = doc  # storing the document in a variable

# Print the first paragraph (for demonstration purposes)
print(docx_output.paragraphs[0].text)  # printing the text of the first paragraph
```

Explanation:
1. The code imports the `Document` class from the `docx` module and the `BeautifulSoup` class for parsing HTML content.
2. An HTML content string is provided as a sample.
3. A new Word document `doc` is created using the `Document` class.
4. The HTML content is parsed using BeautifulSoup to extract text and formatting.
5. The code iterates through 'h1' and 'p' tags in the HTML content and adds headings or paragraphs to the Word document based on the tag type.
6. The resulting document is stored in the variable `docx_output`.
7. For demonstration purposes, the text of the first paragraph in the document is printed.