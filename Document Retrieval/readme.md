# Hybrid  Document Retrieval

## Introduction
This notebook demonstrates the implementation of a document retrieval system using a hybrid technique that combines keyword-based and embedding-based retrieval methods.This system is designed to extract relevant documents from a corpus efficiently and accurately in response to user queries. The system is built using the Haystack library and leverages the strengths of both approaches to provide more accurate and diverse results.

## Components Used
This notebbok utilizes the following components:

1. **DocumentSplitter**: Splits documents into smaller units for processing.
2. **SentenceTransformersDocumentEmbedder**: Embeds document units into dense vector representations using pre-trained models from the Sentence Transformers library.
3. **DocumentJoiner**: Joins document units back together after processing.
4. **InMemoryDocumentStore**: Stores documents and their embeddings in memory for fast retrieval.
5. **InMemoryBM25Retriever**: Performs keyword-based retrieval using the BM25 algorithm, which is effective for matching keywords.
6. **InMemoryEmbeddingRetriever**: Conducts embedding-based retrieval using dense embeddings, which excel in understanding contextual nuances.
7. **TransformersSimilarityRanker**: Ranks retrieved documents based on similarity scores computed using transformer-based models..

## Notebook Overview
Thesystem implementation is structured within a notebook, with the following sections:

1. **Setup**: Installs the required packages for running the notebook.
2. **Data Preparation**: Fetches and processes the data for indexing.
3. **Indexing Documents**: Creates a pipeline to store documents and their embeddings in the document store.
4. **Creating a Hybrid Retrieval Pipeline**: Combines keyword-based and embedding-based retrieval methods to form a hybrid pipeline.
5. **Testing the Hybrid Retrieval Pipeline**: Passes queries to the pipeline and visualizes the retrieved results.

## Usage
To use this notebook for document retrieval, follow these steps:

1. Ensure all required packages are installed by running the setup section of the notebook.
2. Prepare your data by fetching and processing it accordingly.
3. Index the documents using the provided pipeline, which will store them in the document store with their embeddings.
4. Create a hybrid retrieval pipeline by combining the keyword-based and embedding-based retrievers.
5. Test the hybrid retrieval pipeline by passing queries and observing the retrieved results.

## Acknowledgements
This notebook makes use of various open-source libraries and pre-trained models, including Haystack, Sentence Transformers, and Transformers, among others. We acknowledge the contributions of the developers and researchers behind these tools, which have enabled the creation of efficient and powerful document retrieval systems.

## License
This project is licensed under the [MIT License](LICENSE), allowing for modification, distribution, and commercial use under certain conditions. Refer to the license file for more details.
