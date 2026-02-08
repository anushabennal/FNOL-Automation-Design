import axios from "axios";
import { useState } from "react";
import ResultView from "./ResultView";

function UploadForm() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/process-fnol",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          },
          timeout: 30000
        }
      );

      setResult(response.data);
    } catch (err) {
      console.error("Upload error:", err);

      if (err.response) {
        setError(`Backend error: ${err.response.status}`);
      } else if (err.request) {
        setError("Backend not reachable. Is Flask running?");
      } else {
        setError("Unexpected error occurred.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <input type="file" onChange={handleUpload} />

      {loading && <p>Processing FNOL document…</p>}

      {error && (
        <p style={{ color: "red", fontWeight: "bold" }}>
          {error}
        </p>
      )}

      {result && <ResultView result={result} />}
    </div>
  );
}

export default UploadForm;
