# from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_community.embeddings.openai import OpenAIEmbeddings # Importing OpenAIEmbeddings from langchain_community
from langchain_community.embeddings.huggingface import HuggingFaceInstructEmbeddings # Importing HuggingFaceInstructEmbeddings from langchain_community
from langchain_community.vectorstores.faiss import FAISS # Importing FAISS from langchain_community.vectorstores
from langchain_text_splitters import (Language,RecursiveCharacterTextSplitter,) # Importing Language, RecursiveCharacterTextSplitter from langchain_text_splitters
from langchain_openai import OpenAI, ChatOpenAI, OpenAIEmbeddings # Importing OpenAI, ChatOpenAI, OpenAIEmbeddings from langchain_openai
import os # Importing the os module
from langchain.chains.combine_documents import create_stuff_documents_chain # Importing create_stuff_documents_chain from langchain.chains.combine_documents
from langchain_core.prompts import ChatPromptTemplate # Importing ChatPromptTemplate from langchain_core.prompts
from langchain.chains import create_retrieval_chain # Importing create_retrieval_chain from langchain.chains
import streamlit as st # Importing streamlit as st module

@st.cache_data(show_spinner=True) # Cache the function output to avoid recomputation
def llm_response(api_key,  prompt, code, context = "context not available"): # Define the llm_response function taking api_key, prompt, code, and context as input parameters
    
    #------------------------------------------------
    # # Prompt the user for their OpenAI API key
    # api_key = input("insert api key")
    # Set the API key as an environment variable
    os.environ["OPENAI_API_KEY"] = api_key # Setting the OPENAI_API_KEY environment variable with the provided api_key
    print("done! api key") # Print a message indicating the api key is set successfully

    #---------------------------------------------------
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100, # Setting the chunk size to 100
    chunk_overlap=20, # Setting the chunk overlap to 20
    length_function=len, # Using the len function to calculate length
    is_separator_regex=False, # Setting separator regex to False
    )

    texts = text_splitter.split_text(context) # Splitting the text based on the context
    # print(texts)
    #-------------------------------------------------

    # Create vector store
    embeddings = OpenAIEmbeddings(api_key= api_key) # Creating OpenAIEmbeddings with the provided api_key

    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings) # Creating a Faiss vector store based on the text and embeddings

    #---------------------------------------------------
    # Create conversation chain
    # llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo",max_tokens=7000)
    llm = ChatOpenAI(api_key=api_key, model ="gpt-3.5-turbo-0125", max_tokens=4000) # Creating a ChatOpenAI instance with the specified parameters

    
    prompt_template = ChatPromptTemplate.from_template("""Answer the following question based only on the provided code:
    <context>{context}</context>
    Question: {input}
    Code: {code}""") # Creating a prompt template for chat interactions
    document_chain = create_stuff_documents_chain(llm, prompt_template) # Creating a document chain for chat interactions

    retriever = vectorstore.as_retriever() # Converting the vector store to a retriever
    retrieval_chain = create_retrieval_chain(retriever, document_chain) # Creating a retrieval chain for the conversation

    response = retrieval_chain.invoke({"input": f"""{prompt}""", "code": f"{code}"}) # Invoking the retrieval chain with the provided prompt and code
    print(response["answer"]) # Printing the response answer
    final_response = response["answer"] # Storing the final response
    return final_response # Returning the final response


# prompt = "Create the code documentation for the provided code in Markdown format// for a new commer to understand easily, elaborate every part of the code// start by writing title as code documentation"

# context="""
# push_to_confluence.py file is created to push the markdown format file into the confluence page.
# Since we can't push markdown format file directly in to the confluence page we need to convert the markdown format file into html
# then push it to confluence, we need to ask the User to input, confluence url, space key, username, api_token, then we will put those values into the 
# cofluence function and push it to confluence by create an new page if it dosen't exist already, if it exists throw an error that it already exists. 
# """
# code = """
# import requests
# import json
# import base64
# import markdown
# import streamlit as st


# def clear_submit():
#     st.session_state["submit"] = True

# # function
# def confluence(confluence_url,space_key,username,api_token,page_title,mark_data):
    
#     #reading file and string in into a variable
#     # with open(uploaded_file.name, 'r') as file:
#     #     mark_data = file.read()
        
#     # Convert markdown to HTML
#     html_text = markdown.markdown(mark_data)
    
#     # Prepare data for the API request
#     data = {
#         "type": "page",
#         "title": page_title,
#         "space": {"key": space_key},
#         "body": {
#             "storage": {
#                 "value": html_text,
#                 "representation": "storage"
#             }}}

#     url = f"{confluence_url}/rest/api/content"
#     # Send the POST request to create the page
#     headers = {
#     "Authorization": f"Basic {base64.b64encode(f'{username}:{api_token}'.encode()).decode()}",
#     "X-Atlassian-Token": api_token,"Content-Type": "application/json"}


#     response = requests.post(url, json=data, headers=headers)
#     print(response.status_code)

#     # Check for success
#     if response.status_code == 200:
#         st.success(f"{page_title} created successfully!", icon="✅")
#         print("Page created successfully!")
#     elif response.status_code == 400:
#         st.error(f"{page_title} already exist:")
#         print("Error creating page:", response.text)
#     else:
#         st.write("Error creating page:", response.text)
#         print("Error creating page:", response.text)


# # calling function with inputs
# # with st.sidebar:
       
# #     confluence_url = st.text_input("Confluence URL", )  
# #     space_key = st.text_input("Space Key", )  
# #     username = st.text_input("User Name", )   
# #     api_token = st.text_input("API Key", ) 
# #     page_title = st.text_input("Page Title", ) 
#     # uploaded_file = st.file_uploader("Upload file",type=['txt','md'],help="Only txt,md  files are supported",)   
    
# # if uploaded_file:
# #     confluence(confluence_url,space_key,username,api_token,page_title,uploaded_file)
# """

# llm_response('', prompt=prompt, code=code, context=context)