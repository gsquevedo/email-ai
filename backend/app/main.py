from dotenv import load_dotenv
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.file_reader import read_pdf, read_txt
from app.nlp import preprocess_text
from app.ai_service import classify_email, generate_reply

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

app = FastAPI(title="Email Classification API")

# CORS para React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/process-email")
async def process_email(
    emailText: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    if not emailText and not file:
        raise HTTPException(status_code=400, detail="Nenhum conteúdo enviado.")

    if file:
        if file.filename.endswith(".pdf"):
            content = read_pdf(file)
        elif file.filename.endswith(".txt"):
            content = read_txt(file)
        else:
            raise HTTPException(status_code=400, detail="Formato inválido.")
    else:
        content = emailText

    try:
        processed_text = preprocess_text(content)
        category = classify_email(processed_text)
        print("Categoria:", category)

        reply = generate_reply(content, category)
    except Exception as e:
        print("Erro ao processar o email com IA.", str(e))
        raise HTTPException(
            status_code=503,
            detail="Erro ao processar o email com IA."
        )

    return {
        "categoria": category,
        "resposta_sugerida": reply,
    }
