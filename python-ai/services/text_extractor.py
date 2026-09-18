import io
import re
import logging

logger = logging.getLogger(__name__)

def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    """
    Extracts plain text from raw PDF bytes using pypdf.
    Falls back to regex text extraction if pypdf fails.
    """
    extracted_text = ""
    try:
        from pypdf import PdfReader
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_file)
        pages_text = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                pages_text.append(t)
        extracted_text = "\n".join(pages_text)
    except Exception as e:
        logger.warning(f"pypdf extraction failed, attempting fallback: {e}")
        # Fallback text extraction for basic PDF streams
        try:
            raw_str = pdf_bytes.decode('latin-1', errors='ignore')
            # Extract ascii word chunks from raw PDF bytes
            chunks = re.findall(r'[A-Za-z0-9\+\#\.\,\-\s]{3,}', raw_str)
            extracted_text = " ".join(chunks)
        except Exception as ex:
            logger.error(f"Fallback extraction failed: {ex}")
            extracted_text = ""

    return cleaned_text(extracted_text)

def cleaned_text(text: str) -> str:
    if not text:
        return ""
    # Normalize whitespace
    text = re.sub(r'\r\n|\r', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()
