from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import extract_text
from extractor import extract_fields
from router import route_claim
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/process-fnol", methods=["POST"])
def process_fnol():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        file_bytes = file.read()

        text = extract_text(file_bytes, file.filename)
        fields = extract_fields(text)
        route, missing, reason = route_claim(fields)

        return jsonify({
            "extractedFields": fields,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": reason
        })

    except Exception as e:
        print("BACKEND ERROR:")
        traceback.print_exc()
        return jsonify({
            "error": "Backend processing failed",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
