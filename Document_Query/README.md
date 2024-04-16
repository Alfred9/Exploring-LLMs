# Document Knowledge Retrieval

**Note:** An online version of this application is hosted on Streamlit and can be accessed at [Document Query Using LLM](https://document-query-using-llm.streamlit.app/). If you prefer to use the hosted version, you can access it via the provided link.


Welcome to Document Knowledge Retrieval, a Python application powered by Streamlit for querying and extracting knowledge from documents. This application enables you to upload documents in either .docx or .txt format and ask questions about their content using pre-trained language models.

## Prerequisites

Before running this application, make sure you have the required dependencies installed. You can install them using `pip`:

```bash
pip install streamlit
pip install python-docx
pip install langchain
```

You will also need to obtain an API token from Hugging Face and replace the `huggingfacehub_api_token` variable in the code with your own API token.

## Usage

Follow these steps to run the Document Knowledge Retrieval application on your local machine:

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory where the code is located.

3. Run the following command to start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. This will launch a local web application. You can access it through your web browser by following the provided URL.

5. On the application's web interface, you can:

   - **Select a Language Model (LLM):** Choose a language model from the dropdown menu.
   - **Upload a Document:** Upload a document in either .docx or .txt format.
   - **Ask Questions:** Pose questions about the content of the uploaded document.
   - **View Responses:** See the model's responses to your questions.

6. Enjoy using Document Knowledge Retrieval to interact with your documents and gain insights from them!

## Notes

- This application provides an intuitive user interface for querying documents using pre-trained language models.

- You have the flexibility to customize the layout and appearance of the Streamlit app by modifying the code to suit your preferences.

- Be aware of the terms of use and any associated costs when using external services, such as the Hugging Face model hub.

- Ensure that you have the appropriate permissions to use and access the document content.

- For any questions or issues related to this application, feel free to reach out to the developer for support.

## Acknowledgments

This application is powered by the [Hugging Face Transformers library](https://huggingface.co/transformers/), Streamlit, and other open-source tools and libraries.

Enjoy using Document Knowledge Retrieval for your document analysis and information retrieval needs!

---

**Important:** Please remember to keep your API token secure and do not share it publicly. You can store it in a secure environment or use environment variables for added security.
```
