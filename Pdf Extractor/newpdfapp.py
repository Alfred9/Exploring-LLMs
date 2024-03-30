import PyPDF2
import re
import docx
import email
import streamlit as st

def extract_text_from_pdf(file):
    pdf_file = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    pdf_file.close()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def extract_text_from_email(raw_email):
    email_message = email.message_from_bytes(raw_email)
    text = ""
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                text += part.get_payload().decode("utf-8")
    else:
        text = email_message.get_payload().decode("utf-8")
    return text

def extract_info(text):
    invoice_number = re.search(r"Invoice\s+Number:\s*(\w+)", text)
    if invoice_number:
        invoice_number = invoice_number.group(1)

    company_name_and_address = re.search(r"Company\s+Name:\s*(.*?)\s+Address:\s*(.*?)\s*", text, re.DOTALL)
    if company_name_and_address:
        company_name_and_address = (company_name_and_address.group(1), company_name_and_address.group(2))

    seller_dispatcher_details = re.search(r"Seller/Dispatcher\s+Details:\s*(.*?)\s*", text, re.DOTALL)
    if seller_dispatcher_details:
        seller_dispatcher_details = seller_dispatcher_details.group(1)

    delivery_address = re.search(r"Delivery\s+Address:\s*(.*?)\s*", text, re.DOTALL)
    if delivery_address:
        delivery_address = delivery_address.group(1)

    dates = re.findall(r"(\b\d{2}/\d{2}/\d{4}\b)", text)

    return {
        "invoice_number": invoice_number,
        "company_name_and_address": company_name_and_address,
        "seller_dispatcher_details": seller_dispatcher_details,
        "delivery_address": delivery_address,
        "dates": dates
    }

def main():
    st.set_page_config(page_title="Document Info Extractor", page_icon=":guardsman:", layout="wide")

    st.title("Document Information Extractor")
    st.subheader("Select a file or email")

    file_type = st.radio("", ["PDF", "Word Docx", "Email"], index=0)

    if file_type == "PDF":
        file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if file:
            text = extract_text_from_pdf(file)
            result = extract_info(text)
            display_result(result)
    elif file_type == "Word Docx":
        file = st.file_uploader("Upload a Word Docx file", type=["docx"])
        if file:
            text = extract_text_from_docx(file)
            result = extract_info(text)
            display_result(result)
    elif file_type == "Email":
        file = st.file_uploader("Upload an email file", type=["eml"])
        if file:
            raw_email = file.read()
            text = extract_text_from_email(raw_email)
            result = extract_info(text)
            display_result(result)

def display_result(result):
    st.subheader("Extracted Information")
    st.write("Invoice Number: ", result["invoice_number"])
    st.write("Company Name and Address: ", result["company_name_and_address"])
    st.write("Seller/Dispatcher Details: ", result["seller_dispatcher_details"])
    st.write("Delivery Address: ", result["delivery_address"])
    st.write("Dates: ", result["dates"])

if __name__ == "__main__":
    main()
