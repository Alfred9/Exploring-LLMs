## Generative Question Answering (QA)
## Introduction
Generative Question Answering (QA) involves creating novel text answers rather than just extracting them from a given context. This project utilizes the RAGenerator model to set up a generative QA system that conditions the answer generator on a set of retrieved documents.

RAGenerator combines the strengths of retrieval-based methods (efficiently retrieving relevant information) with generative methods (flexibility in generating answers) to provide more accurate and informative responses to questions. It's particularly useful in scenarios where the information required to answer questions is spread across a large corpus, such as open-domain question answering or complex information retrieval tasks.

## Tools Used
- Haystack: A framework for building end-to-end question answering systems.
- Dense Passage Retriever (DPR): Used for retrieving relevant documents.
- RAGenerator: Utilized for generating novel text answers based on retrieved documents.

## Project Overview
The project involves the following steps:
1. Fetching and cleaning documents: Downloading a sample dataset and preprocessing the data.
2. Initializing Components: Setting up the DocumentStore, Retriever, Generator, and Pipeline.
3. Asking Questions: Interacting with the system by asking questions and retrieving generative answers.


## Additional Details
- Telemetry: Anonymous usage statistics are collected for base components.
- Logging: Logging messages are configured to display and utilize appropriate log levels.
- Dependencies: Ensure that all necessary dependencies are installed using pip.



