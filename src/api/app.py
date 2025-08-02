from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
from src.utils.parser import extract_text_docx, extract_text_image
from src.llm.extractor import extract_metadata

app = FastAPI()

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    suffix = file.filename.split(".")[-1]
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}")
    temp_file.write(await file.read())
    temp_file.close()

    if suffix == "docx":
        text = extract_text_docx(temp_file.name)
    elif suffix in ["png", "jpg", "jpeg"]:
        text = extract_text_image(temp_file.name)
    else:
        return JSONResponse(content={"error": "Unsupported file format"}, status_code=400)

    result = extract_metadata(text)
    return JSONResponse(content={"metadata": eval(result)})