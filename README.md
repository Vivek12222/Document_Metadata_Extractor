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


## 🧠 How It Works – Behind the Scenes
<b>🧾 Step 1: Extract Text from Documents</b>
  .docx files are parsed using python-docx
  .png images are processed using pytesseract OCR

<b>💬 Step 2: Prompt LLM via LangChain</b>
A text prompt (from prompt_template.txt) is filled with the extracted raw text

Google Gemini Pro interprets the document and extracts:

1. Agreement Start Date
2. Agreement End Date
3. Agreement Value
4. Party One
5.  Party Two
6. Renewal Notice (Days)

<b>📄 Step 3: Save Metadata</b>
The extracted data is saved to output/test_predictions.csv


## ⚙️ Setup Instructions (Beginner-Friendly)
🖥️ Works on Windows, Mac, Linux
🧠 No prior ML or AI knowledge needed

✅ 1. Clone the Repository
<pre>
git clone https://github.com/your-username/Document_MetaData_Extractor.git
cd Document_MetaData_Extractor
</pre>

📦 2. Create a Virtual Environment
<pre>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
</pre>

🔑 3. Set Google Gemini API Key
Create a .env file (if not present) and add your API key:
<pre>
GOOGLE_API_KEY=your_actual_gemini_api_key
</pre>

📁 4. Add Test Files
1. Place your .docx and .png rental agreements inside data/test/
2. Ensure data/test.csv has the ground truth metadata for evaluation

## 🚀 Run Predictions
This runs the full pipeline: parses input files → sends to LLM → saves structured output.

<pre>
python predict.py
</pre>
✅ Output will be stored in: output/test_predictions.csv

## 📊 Evaluate Performance (Recall)
You can compare LLM predictions with the correct answers using:

<pre>
python evaluate.py
</pre>
✅ This prints per-field recall and macro average recall.


<img width="396" height="204" alt="Screenshot 2025-08-02 101415" src="https://github.com/user-attachments/assets/4362abdc-181a-4d2b-95b3-6ceab8d25a14" />

## 🌐 Run as REST API (Optional)
The system is optionally wrapped as a REST API using FastAPI.

▶️ Start API Server
<pre>
uvicorn src.api.app:app --reload
Server runs at: http://127.0.0.1:8000
</pre>

🔍 Endpoint: /extract-metadata
Method: POST
Request Body:

<pre>
{
  "text": "Raw document text goes here..."
}
</pre>
Response:

<pre>
{
  "Agreement Start Date": "...",
  "Agreement End Date": "...",
  "Agreement Value": "...",
  ...
}
</pre>
You can integrate this with Postman, web apps, or other services.

## 💡 Key Features
✅ No rule-based parsing or regular expressions
✅ Supports .docx and .png files
✅ Modular structure for easy extension
✅ REST API ready for production
✅ Evaluation metrics for performance tracking

## 📚 Terminologies (Made Simple)
Term	What it Means
1. LLM	Large Language Model — AI that understands human-like text
2. LangChain —	A tool to talk to LLMs in a structured way
3. OCR	Extracts text from scanned images
4. Prompt — 	Instruction to tell the AI what to do
5. FastAPI — 	Tool to turn Python code into APIs

## ✨ Future Enhancements
1. Add .pdf support via pdfminer or PyMuPDF
2. Switch between Gemini, GPT-4, Claude dynamically
3. Add a front-end UI to upload files directly
4. Include confidence scores from the LLM
