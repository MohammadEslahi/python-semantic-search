# Python Semantic Search

A beginner-friendly semantic search project built with Python and Sentence Transformers.

This project explores how machines can understand the meaning of text by converting sentences into numerical embeddings and comparing their semantic similarity.

## Features

- Generate text embeddings using a pretrained Sentence Transformer model.
- Calculate semantic similarity using cosine similarity.
- Find the closest matching sentence with a custom `find_closest()` function.
- Retrieve the top 2 most relevant sentences using `util.semantic_search()`.

## Technologies

- Python
- Sentence Transformers
- PyTorch

## Pretrained Model

This project uses:

`sentence-transformers/all-MiniLM-L6-v2`

The model converts text into 384-dimensional numerical embeddings.

## Installation

Clone the repository:

```bash
git clone https://github.com/MohammadEslahi/python-semantic-search
cd python-semantic-search
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The program compares a query with a collection of sentences and retrieves the two most semantically similar results.

## Learning Objectives

Through this project, I practiced:

- Understanding Text Embeddings
- Semantic Similarity
- Cosine Similarity
- Semantic Search
- Working with pretrained Transformer models

## Author

Mohammad Eslahi