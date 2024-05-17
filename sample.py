```python
# Import necessary modules
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import (Language, RecursiveCharacterTextSplitter, )
from langchain_openai import OpenAI, ChatOpenAI, OpenAIEmbeddings
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import streamlit as st

# Define function llm_response to generate responses
@st.cache_data(show_spinner=True)
def llm_response(api_key, prompt, code, context = "context not available"):
    
    # Set the API key as an environment variable
    os.environ["OPENAI_API_KEY"] = api_key
    print("done! api key")

    # Define text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )

    texts = text_splitter.split_text(context)

    # Create vector store using OpenAIEmbeddings
    embeddings = OpenAIEmbeddings(api_key=api_key)
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)

    # Create conversation chain using ChatOpenAI
    llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo-0125", max_tokens=4000)
    
    # Define ChatPromptTemplate
    prompt_template = ChatPromptTemplate.from_template("""Answer the following question based only on the provided code:
    <context>{context}</context>
    Question: {input}
    Code: {code}""")
    
    document_chain = create_stuff_documents_chain(llm, prompt_template)

    # Create retriever and retrieval chain
    retriever = vectorstore.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Invoke retrieval chain and get response
    response = retrieval_chain.invoke({"input": f"""{prompt}""", "code": f"{code}"})
    print(response["answer"])
    final_response = response["answer"]
    return final_response

# Define prompt and context
prompt = "Create the code documentation for the provided code in Markdown format// for a new commer to understand easily, elaborate every part of the code// start by writing title as code documentation"

context="""
push_to_confluence.py file is created to push the markdown format file into the confluence page.
Since we can't push markdown format file directly in to the confluence page we need to convert the markdown format file into html
then push it to confluence, we need to ask the User to input, confluence url, space key, username, api_token, then we will put those values into the 
cofluence function and push it to confluence by create an new page if it dosen't exist already, if it exists throw an error that it already exists.
"""
# Define code that needs to be documented
code = """
import requests
import json
import base64
import markdown
import streamlit as st

# Function to clear submit
def clear_submit():
    st.session_state["submit"] = True

# Function to push content to Confluence
def confluence(confluence_url, space_key, username, api_token, page_title, mark_data):
    
    # Convert markdown to HTML
    html_text = markdown.markdown(mark_data)
    
    # Prepare data for the API request
    data = {
        "type": "page",
        "title": page_title,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": html_text,
                "representation": "storage"
            }
        }
    }

    url = f"{confluence_url}/rest/api/content"
    # Send the POST request to create the page
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{username}:{api_token}'.encode()).decode()}",
        "X-Atlassian-Token": api_token,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)

    # Check for success
    if response.status_code == 200:
        st.success(f"{page_title} created successfully!", icon="✅")
        print("Page created successfully!")
    elif response.status_code == 400:
        st.error(f"{page_title} already exist:")
        print("Error creating page:", response.text)
    else:
        st.write("Error creating page:", response.text)
        print("Error creating page:", response.text)

# Call the llm_response function with defined inputs
llm_response('', prompt=prompt, code=code, context=context)
```