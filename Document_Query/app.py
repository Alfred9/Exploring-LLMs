import os
import streamlit as st 
from docx import Document
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Replace this with your own Hugging Face API token
huggingfacehub_api_token = st.secrets["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"]

# Customize the layout
st.set_page_config(page_title="Document Query", page_icon=":book:", layout="wide", )     

def write_text_file(content, file_path):
    """
    Write text content to a file.

    Parameters:
    content (str): The text content to be written to the file.
    file_path (str): The path to the file where content will be saved.

    Returns:
    bool: True if writing was successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error occurred while writing the file: {e}")
        return False

def is_docx_file(file):
    """
    Check if a file is in .docx format.

    Parameters:
    file: The uploaded file object.

    Returns:
    bool: True if the file is a .docx file, False otherwise.
    """
    if file.name.split(".")[-1].lower() == "docx":
        return True
    else:
        return False

#  Set prompt template for language model queries
prompt_template = """
You are an artificial intelligence assistant giving helpful, detailed, and polite answers to the user's questions. Below is some information. 
{context}

Based on the above information only, answer the below question. 

{question}
"""

prompt = PromptTemplate.from_template(prompt_template)

# Streamlit app title and additional info
st.title("📚 Document Knowledge Retrieval")
st.markdown("Welcome to Document Knowledge Retrieval! Upload a document and ask questions about its content.")
st.text("Powered by Falcon-7B")


option = st.selectbox(
    'Which LLM would you like to use?',
    ('Falcon-7B', 'Dolly-v2-3B'))


model_dict = {'Falcon-7B': "tiiuae/falcon-7b-instruct", 'Dolly-v2-3B': "databricks/dolly-v2-3b"}

# Set the repo_id based on the chosen LLM
repo_id = model_dict[option] if option else "tiiuae/falcon-7b-instruct"

# Initialize HuggingFaceHub and language model
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token, 
                     repo_id=repo_id, 
                     model_kwargs={"temperature":0.6, "max_new_tokens":250 if option=='Dolly-v2-3B' else 500 })

# Initialize HuggingFaceEmbeddings for text embeddings
embeddings = HuggingFaceEmbeddings()

# Create the LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# File upload section
uploaded_file = st.file_uploader("Upload an article", type=["docx", "txt"])
flag = 0

if uploaded_file is not None:
    if is_docx_file(uploaded_file):
        document = Document(uploaded_file)
        paragraphs = [p.text for p in document.paragraphs]
        
        content = "\n".join(paragraphs)
        file_path = "temp/file.txt"
        write_text_file(content, file_path)   
    else:
        content = uploaded_file.read().decode('utf-8')
        file_path = "temp/file.txt"
        write_text_file(content, file_path)   
    loader = TextLoader(file_path)
    docs = loader.load()    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=256, chunk_overlap=0, separators=[" ", ",", "\n", "."]
    )
    texts = text_splitter.split_documents(docs)
    db = Chroma.from_documents(texts, embeddings)    
    st.success("File Loaded Successfully!!")
    flag = 1

# Query through LLM    
if flag == 1:
    question = st.text_input("Ask something from the file", placeholder="Find something similar to: ....this.... in the text?", disabled=not uploaded_file)    
    if question:
        similar_doc = db.similarity_search(question, k=1)
        context = similar_doc[0].page_content
        query_llm = LLMChain(llm=llm, prompt=prompt)
        response = query_llm.run({"context": context, "question": question})        
        st.write(response)
