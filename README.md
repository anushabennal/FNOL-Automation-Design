# FNOL Claim Processing Agent

## Overview
The FNOL (First Notice of Loss) Claim Processing Agent is a full-stack web application that automates the initial processing of insurance claims.  
It extracts key information from FNOL documents using OCR, validates mandatory fields, and routes claims to the appropriate workflow with a clear explanation.

---

## System Architecture

User uploads FNOL document  
→ React frontend sends file to backend  
→ Flask backend performs OCR  
→ Extracts claim fields  
→ Validates mandatory data  
→ Applies routing rules  
→ Returns routing decision and reasoning

---

## Technologies Used

Frontend:
- React.js
- Axios

Backend:
- Python Flask
- Flask-CORS
- EasyOCR
- pdf2image (for PDF support)
- Pillow (image handling)

---

## Project Structure

FNOL-AGENT  
├── backend  
│   ├── app.py  
│   ├── ocr.py  
│   ├── extractor.py  
│   ├── router.py  
│   └── requirements.txt  
│  
├── frontend  
│   ├── public  
│   │   └── index.html  
│   ├── src  
│   │   ├── App.js  
│   │   ├── UploadForm.js  
│   │   ├── ResultView.js  
│   │   └── index.js  
│   └── package.json  

---

## How the Code Runs

1. User uploads an FNOL document (image or PDF) using the frontend.
2. React sends the file to the Flask backend as a POST request.
3. The backend performs OCR using EasyOCR.
4. Extracted text is processed to identify FNOL fields.
5. Mandatory fields are validated.
6. A rule-based routing engine decides the claim workflow.
7. The backend sends a JSON response.
8. The frontend displays the routing decision and explanation.

---

## Claim Routing Rules

- Manual Review: If mandatory fields are missing
- Fast-Track: If estimated damage is below ₹25,000
- Investigation Flag: If suspicious keywords are detected
- Specialist Queue: If the claim type involves injury

Each routing decision includes a clear explanation.

---

## How to Run the Project

Backend:
1. Open terminal
2. Navigate to backend folder
3. Create and activate virtual environment
4. Install dependencies
5. Run Flask server

Commands:
cd backend  
python -m venv venv  
venv\\Scripts\\activate  
pip install -r requirements.txt  
python app.py  

Backend runs on:
http://127.0.0.1:5000

---

Frontend:
1. Open another terminal
2. Navigate to frontend folder
3. Install dependencies
4. Start React app

Commands:
cd frontend  
npm install  
npm start  

Frontend runs on:
http://localhost:3000

---

## Supported File Types

- JPG
- PNG
- PDF (requires Poppler on Windows)

---

## Sample Output

{
  "extractedFields": {
    "policyNumber": "contact",
    "claimType": "auto",
    "description": "acord additional remarks",
    "location": "police department contacted"
  },
  "missingFields": [
    "dateOfLoss",
    "estimatedDamage",
    "attachments"
  ],
  "recommendedRoute": "Manual Review",
  "reasoning": "Mandatory fields missing"
}

---

## Use Case

This project demonstrates real-world FNOL claim intake automation by reducing manual review effort and enabling intelligent claim routing based on document completeness.

---

## Status

- End-to-end working
- Frontend and backend connected
- OCR-based extraction implemented
- Ready for demo and interview

---


