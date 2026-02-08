import easyocr
import numpy as np
from pdf2image import convert_from_bytes
from PIL import Image
import io

# Initialize EasyOCR once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(file_bytes, filename):
    """
    Extract text from PDF or image using EasyOCR.
    Never raises exception (safe for backend).
    """
    text = ""

    try:
        # -------- PDF HANDLING --------
        if filename.lower().endswith(".pdf"):
            images = convert_from_bytes(file_bytes, dpi=200)

            for img in images:
                img_np = np.array(img)
                results = reader.readtext(img_np)

                for _, txt, _ in results:
                    text += txt + " "

        # -------- IMAGE HANDLING --------
        else:
            image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
            img_np = np.array(image)

            results = reader.readtext(img_np)
            for _, txt, _ in results:
                text += txt + " "

    except Exception as e:
        print("OCR ERROR:", e)
        return ""

    return text.lower()
