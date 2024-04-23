##  Document Retrieval with Hybrid Technique
This notebook demonstrates the implementation of a document retrieval system using a hybrid technique that combines keyword-based and embedding-based retrieval methods. The system is built using the Haystack library and leverages the strengths of both approaches to provide more accurate and diverse results.

https://colab.research.google.com/drive/1wA6hmbFntxMNjnjwWZPiWjvtiyApmRAb#scrollTo=27m-cvtKA_b_

###Requirements
To run this notebook, install the following packages:

!pip install haystack-ai
!pip install "datasets >=2.6.1"
!pip install "sentence-transformers >=2.2.0"
!pip install accelerate

## Document Retrieval
Document retrieval is the art of extracting relevant documents from a corpus in response to an input query. In this notebook, we use a hybrid retrieval technique that combines keyword-based and embedding-based retrieval methods.

## Hybrid Retrieval
Hybrid retrieval combines the strengths of keyword-based and embedding-based retrieval techniques. Dense embeddings excel in understanding the contextual nuances of the query, while keyword-based methods excel in matching keywords.

## Notebook Overview
Setup: Install the required packages.
Data Preparation: Fetch and process the data.
Indexing Documents: Create a pipeline to store the data in the document store with their embeddings.
Creating a Hybrid Retrieval Pipeline: Combine keyword-based and embedding-based retrieval methods for more accurate and diverse results.
Testing the Hybrid Retrieval Pipeline: Pass a query to the pipeline and visualize the results.
