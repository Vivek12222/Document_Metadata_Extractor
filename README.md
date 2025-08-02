# 🧠 AI-Powered Document Metadata Extraction with LangChain + Gemini

## Overview
This project showcases a modern AI-based system that extracts structured metadata (like "Agreement Start Date", "Party One", etc.) from rental agreements and similar documents. Unlike traditional approaches, it does not use regex or rule-based extraction. Instead, it uses Google Gemini Pro LLM via LangChain to infer the required information from natural language, including .docx and .png documents.

The system also includes an optional FastAPI-based REST API, making it suitable for use as a microservice in real-world applications.

## Project Goals
Extract structured metadata from semi-structured/unstructured documents such as:
1. Word files (.docx)
2. Scanned images (.png)

The extracted metadata is saved in CSV format or can be returned via API.

This project is especially valuable for:

1. Legal document automation
2. Business workflows (contract management)
3. Digitizing scanned archives

## 📁 Updated Project Structure
Your project is organized like this:
<img width="727" height="698" alt="Screenshot 2025-08-02 100505" src="https://github.com/user-attachments/assets/83f8bfad-c7c1-4ed5-b3df-12ce7e5d0de2" />

