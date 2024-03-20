# Keyword Extraction with Mistral 7B

## Overview
Keyword extraction is a vital task in natural language processing (NLP), facilitating efficient understanding and analysis of textual data. This notebook explores keyword extraction techniques, focusing on leveraging the Mistral 7B model.

## Tools and Models Used
- **Mistral 7B Model**: The Mistral 7B model is employed for keyword extraction. It is a language model trained on a large corpus of text data and fine-tuned for text generation tasks.
- **Sentence Transformers**: Sentence Transformers is used for extracting embeddings from textual documents, enabling better keyword extraction.
- **KeyBERT**: KeyBERT is utilized for keyword extraction from text using the Mistral 7B model and Sentence Transformers.

## Steps
1. **Package Installation**: Install required packages, including Sentence Transformers and KeyBERT, using pip.
2. **Model Setup**: Load the Mistral 7B model for text generation and configure the GPU acceleration if available.
3. **Huggingface Transformers Pipeline**: Set up a Huggingface Transformers pipeline for text generation tasks using the Mistral 7B model.
4. **Prompt Engineering**: Test the model with a basic example prompt and evaluate its ability to generate relevant text.
5. **Keyword Extraction with Mistral 7B**: Generate a prompt containing a document and instructions for keyword extraction. Extract keywords using Mistral 7B and evaluate the results.
6. **Embedding Extraction**: Utilize Sentence Transformers to extract embeddings from the document.
7. **Keyword Extraction with KeyBERT**: Use KeyBERT to extract keywords from the document using Mistral 7B and the extracted embeddings.

## Usage
1. Open the notebook in Google Colab and execute each cell sequentially.
2. Experiment with different prompts and documents to observe the performance of the keyword extraction techniques.
3. Adjust parameters such as threshold values for keyword extraction to fine-tune the results according to specific requirements.

## Acknowledgements
- This notebook utilizes the Mistral 7B model developed by TheBloke and the Sentence Transformers library.
- KeyBERT is developed by Maarten Grootendorst and sourced from the KeyBERT repository.


