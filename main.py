import os
import tempfile
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from src.utils.parser import extract_text_docx, extract_text_image
from src.llm.extractor import extract_metadata


app = FastAPI(title="Document Metadata Extractor API")

@app.post("/extract-metadata/")
async def extract_metadata_api(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        if suffix == ".docx":
            text = extract_text_docx(tmp_path)
        elif suffix == ".png":
            text = extract_text_image(tmp_path)
        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type"})

        metadata = extract_metadata(text)
        return {"filename": file.filename, "metadata": metadata}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})