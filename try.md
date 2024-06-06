# Code Documentation

## Introduction
This code demonstrates how to create a Word document from HTML content and parse it using BeautifulSoup. The code extracts text and formatting from specific HTML tags and adds them to the Word document.

## Code Structure
1. Import necessary modules:
    - `Document` class from the `docx` module
    - `BeautifulSoup` for parsing HTML content
    
2. Define the HTML content:
    - A sample HTML content with a heading and a paragraph
    
3. Create a new Word document:
    - Initialize an instance of the `Document` class
    
4. Parse the HTML content:
    - Use BeautifulSoup to parse the HTML content
    
5. Extract and add text and formatting to the document:
    - Iterate through 'h1' and 'p' tags in the HTML content
    - Add headings and paragraphs to the document based on the tag type
    
6. Save the document in memory:
    - Store the document in a variable `docx_output`
    
7. Print the first paragraph:
    - For demonstration purposes, print the text of the first paragraph in the document

## Usage
This code can be used to convert HTML content into a Word document, preserving the structure and formatting of the original content. It provides a simple way to automate the creation of formatted documents from HTML sources.