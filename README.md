📌 Overview

The FNOL (First Notice of Loss) Claim Processing Agent is a full-stack web application designed to automate the initial intake and routing of insurance claims.
It uses OCR to extract information from FNOL documents, validates mandatory fields, and routes claims to the appropriate workflow with a clear explanation.

🏗️ System Architecture
User (Browser)
   ↓
React Frontend (File Upload UI)
   ↓ HTTP POST (multipart/form-data)
Flask Backend API
   ↓
OCR (EasyOCR)
   ↓
Field Extraction & Validation
   ↓
Rule-Based Routing Engine
   ↓
JSON Response (Route + Reason)

⚙️ Technologies Used
Frontend

React.js – User interface and SPA

Axios – HTTP communication with backend

Backend

Python Flask – REST API server

Flask-CORS – Cross-origin communication

EasyOCR – Optical Character Recognition

pdf2image – PDF to image conversion (optional)

Pillow (PIL) – Image processing

📂 Project Structure
FNOL-AGENT/
├── backend/
│   ├── app.py          # Flask API entry point
│   ├── ocr.py          # OCR logic (PDF/Image handling)
│   ├── extractor.py   # FNOL field extraction
│   ├── router.py      # Claim routing rules
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── UploadForm.js
│   │   ├── ResultView.js
│   │   └── index.js
│   ├── package.json

🔄 How the Code Runs (Execution Flow)

The user uploads an FNOL document (image or PDF) from the React UI.

React sends the file to the Flask backend using a POST request.

The backend performs OCR using EasyOCR.

Extracted text is parsed to identify key FNOL fields.

Mandatory fields are validated.

A rule-based engine determines the appropriate claim route.

The backend returns a structured JSON response.

The frontend displays the routing decision and explanation.

🔀 Claim Routing Rules

Manual Review → Mandatory fields missing

Fast-Track → Estimated damage < ₹25,000

Investigation Flag → Fraud-related keywords detected

Specialist Queue → Injury-related claims

Each decision includes a human-readable reason.

🖥️ How to Run the Project
Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


Backend runs at:

http://127.0.0.1:5000

Frontend Setup
cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000

📄 Supported File Types

JPG / PNG (recommended)

PDF (requires Poppler on Windows)

🧪 Sample Output
{
  "extractedFields": {
    "policyNumber": "contact",
    "claimType": "auto",
    "description": "acord 101 additional remarks...",
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

📈 Use Case

This project simulates real-world insurance FNOL automation, reducing manual effort during claim intake and enabling intelligent triaging based on document completeness and risk indicators.

🏁 Status

✅ End-to-end working

✅ Frontend and backend integrated

✅ Stable OCR processing

✅ Interview and demo ready
