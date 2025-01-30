from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import fitz  # PyMuPDF for PDFs
import openai  # Replace with DeepSeek or local LLM as needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    extracted_text = extract_text(file_path)
    return {"filename": file.filename, "content": extracted_text}

def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
    # Add DOCX handling if needed
    return text

@app.post("/interview/")
async def conduct_interview(text: str = Form(...)):
    prompt = f"""
    Act as a Visa Interviewer. Given the following document content:
    {text}

    - Ask relevant questions to determine the candidate's intent to study abroad.
    - Assess if they are likely to return to their home country.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return {"questions": response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
