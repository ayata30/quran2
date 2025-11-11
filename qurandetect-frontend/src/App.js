import React, { useState } from "react";

export default function Home() {
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

    // Step 1 — Transcribe
    const formData = new FormData();
    formData.append("file", audioFile);

    const transcribeRes = await fetch("http://127.0.0.1:8000/transcribe", {
      method: "POST",
      body: formData,
    });

    const transcribeData = await transcribeRes.json();
    const text = transcribeData.text;
    setTranscription(text);

    // Step 2 — Detect Verse
    const detectRes = await fetch("http://127.0.0.1:8000/detect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const detectData = await detectRes.json();
    setMatch(detectData);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-8">
      <h1 className="text-3xl font-bold mb-4">🎧 QuranDetect Local Demo</h1>

      <input
        type="file"
        accept="audio/*"
        onChange={handleUpload}
        className="mb-4"
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-green-600 px-4 py-2 rounded hover:bg-green-700"
      >
        {loading ? "Processing..." : "Upload & Detect"}
      </button>

      {transcription && (
        <div className="mt-6 text-center">
          <h2 className="text-xl font-semibold">🗣️ Transcription:</h2>
          <p className="mt-2 text-gray-300">{transcription}</p>
        </div>
      )}

      {match && match.match && (
        <div className="mt-6 text-center">
          <h2 className="text-xl font-semibold">📖 Closest Match:</h2>
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
