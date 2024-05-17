```python
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import (Language,RecursiveCharacterTextSplitter,)
from langchain_openai import OpenAI, ChatOpenAI, OpenAIEmbeddings
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import streamlit as st

@st.cache_data(show_spinner=True)
def llm_response(api_key,  prompt, code, context = "context not available"):
    
    #------------------------------------------------
    # Prompt the user for their OpenAI API key
    # api_key = input("insert api key")
    # Set the API key as an environment variable
    os.environ["OPENAI_API_KEY"] = api_key
    print("done! api key")

    #---------------------------------------------------
    # Create a RecursiveCharacterTextSplitter object to split the text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )

    texts = text_splitter.split_text(context)
    # print(texts)
    #-------------------------------------------------

    # Create OpenAI Embeddings
    embeddings = OpenAIEmbeddings(api_key= api_key)

    # Create FAISS vectorstore from the text embeddings
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)

    #---------------------------------------------------
    # Create ChatOpenAI model for conversation
    llm = ChatOpenAI(api_key=api_key, model ="gpt-3.5-turbo-0125", max_tokens=4000)

    # Create a ChatPromptTemplate for the response
    prompt_template = ChatPromptTemplate.from_template("""Answer the following question based only on the provided code:
    <context>{context}</context>
    Question: {input}
    Code: {code}""")
    
    # Create document chain for processing documents
    document_chain = create_stuff_documents_chain(llm, prompt_template)

    # Create retriever from vectorstore
    retriever = vectorstore.as_retriever()

    # Create retrieval chain for retrieving documents
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Invoke the retrieval chain with the prompt and code
    response = retrieval_chain.invoke({"input": f"""{prompt}""", "code": f"{code}"})
    print(response["answer"])
    final_response = response["answer"]
    return final_response
```