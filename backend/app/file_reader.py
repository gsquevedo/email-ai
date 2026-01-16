import io
import pdfplumber
from fastapi import UploadFile


def read_txt(file: UploadFile) -> str:
    content = file.file.read()
    return content.decode("utf-8", errors="ignore")


def read_pdf(file: UploadFile) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(file.file.read())) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
