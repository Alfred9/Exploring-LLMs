
import PyPDF2
import spacy
from transformers import pipeline
import streamlit as st

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text



nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return tokens, entities

def extract_information(text):
    model = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")
    prompt = f"Extract the invoice number, company name and address, seller/dispatcher details, delivery address, and dates (invoice date, delivery date) from the following text: {text}"
    response = model(prompt, max_length=512, do_sample=False)
    return response[0]["generated_text"]

def main():
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt", "eml"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file.name)
        elif uploaded_file.type == "application/msword":
            text = extract_text_from_docx(uploaded_file.name)
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode()
        elif uploaded_file.type == "message/rfc822":
            text = extract_text_from_email(uploaded_file.name)
        else:
            st.write("Unsupported file format")
            return
        tokens, entities = preprocess_text(text)
        info = extract_information(text)
        st.write("Invoice Number: ", info.split("\n")[0])
        st.write("Company Name and Address: ", info.split("\n")[1])
        st.write("Seller/Dispatcher Details: ", info.split("\n")[2])
        st.write("Delivery Address: ", info.split("\n")[3])
        st.write("Dates: ", info.split("\n"))


if __name__ == "__main__":
    main()
