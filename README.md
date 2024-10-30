# NCERT RAG System

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-AI-orange)

> A Question-Answering system designed to fetch responses from NCERT material using advanced AI-powered embeddings and retrieval techniques.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

The **NCERT RAG System** is a QA (Question-Answering) platform that allows users to ask questions related to NCERT (National Council of Educational Research and Training) content. By parsing the NCERT PDF materials and applying language models, this project quickly generates relevant answers to user queries.

The project combines:
- **Streamlit** for a user-friendly frontend.
- **FastAPI** for an efficient backend.
- **LangChain** with **Google Generative AI** embeddings and **FAISS** (vector store) for reliable question-answering capabilities.

This tool aims to help students, educators, and researchers efficiently retrieve information directly from NCERT content without needing to manually search through the PDFs.

---

## Features

- **User-friendly Interface**: A simple interface for inputting questions and getting answers.
- **AI-Powered Responses**: Generates answers based on embedded representations of the NCERT material, ensuring relevant responses.
- **PDF Parsing**: Reads the NCERT PDF files and makes the content available for question-answering.
- **Quick Retrieval**: Uses FAISS vector search to speed up response times for large text datasets.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
