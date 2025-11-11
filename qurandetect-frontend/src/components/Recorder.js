import React, { useState } from "react";

export default function Recorder() {
  const [audioFile, setAudioFile] = useState(null);
  const [transcription, setTranscription] = useState("");
  const [match, setMatch] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => {
    setAudioFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!audioFile) return alert("Please upload an audio file first!");
    setLoading(true);

    try {
      // Step 1 — Transcribe
      const formData = new FormData();
      formData.append("file", audioFile);

      const transcribeRes = await fetch("http://127.0.0.1:8000/transcribe", {
        method: "POST",
        body: formData,
      });

      const transcribeData = await transcribeRes.json();
      const text = transcribeData.text || "";
      setTranscription(text);

      // Step 2 — Detect Verse
      const detectRes = await fetch("http://127.0.0.1:8000/detect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const detectData = await detectRes.json();
      setMatch(detectData);
    } catch (err) {
      console.error(err);
      alert("Something went wrong. Check backend logs.");
    }

    setLoading(false);
  };

  return (
    <div className="bg-gray-900 p-8 rounded-2xl shadow-xl text-white max-w-md mx-auto mt-6">
      <h2 className="text-2xl font-bold mb-4">🎧 Upload or Record Audio</h2>

      <input
        type="file"
        accept="audio/*"
        onChange={handleUpload}
        className="mb-4 w-full text-sm text-gray-300"
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-green-600 px-4 py-2 rounded-lg hover:bg-green-700 w-full"
      >
        {loading ? "Processing..." : "Detect Verse"}
      </button>

      {transcription && (
        <div className="mt-6">
          <h3 className="font-semibold text-lg">🗣️ Transcription:</h3>
          <p className="mt-2 text-gray-300">{transcription}</p>
        </div>
      )}

      {match && match.match && (
        <div className="mt-6">
          <h3 className="font-semibold text-lg">📖 Closest Match:</h3>
          <p className="mt-2 text-green-300">
            Surah {match.match.surah}:{match.match.ayah} — {match.match.text}
          </p>
          <p className="mt-1 text-sm text-gray-400">
            Confidence: {match.confidence}%
          </p>
        </div>
      )}
    </div>
  );
}
