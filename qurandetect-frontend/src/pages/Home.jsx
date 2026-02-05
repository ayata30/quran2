import React, { useState } from "react";

export default function Home() {
  const [audioFile, setAudioFile] = useState(null);
  const [transcription, setTranscription] = useState("");
  const [match, setMatch] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => {
    setAudioFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!audioFile) {
      alert("Please upload an audio file first!");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", audioFile);

      const transcribeRes = await fetch(
        "http://127.0.0.1:8000/transcribe",
        {
          method: "POST",
          body: formData,
        }
      );

      const transcribeData = await transcribeRes.json();
      const text = transcribeData.text;
      setTranscription(text);

      const detectRes = await fetch(
        "http://127.0.0.1:8000/detect",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text }),
        }
      );

      const detectData = await detectRes.json();
      setMatch(detectData);
    } catch (err) {
      console.error(err);
      alert("Upload failed. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {/* HERO */}
      <section className="text-center">
        <h1 className="text-3xl font-bold mb-2">
          Detect Any Quran Recitation!
        </h1>
        <p className="text-md mb-4">
          Upload audio and instantly find the Surah & Ayah
        </p>
      </section>

      {/* DETECTION */}
      <section className="mx-auto max-w-md rounded bg-teal-400 p-6 dark:bg-teal-700">
        <h2 className="text-2xl font-bold mb-4 text-center">
          🎧 Try QuranDetect
        </h2>

        <form onSubmit={handleSubmit}>
          <input
            type="file"
            accept="audio/*"
            onChange={handleUpload}
            className="mb-4 w-full"
          />

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-teal-600 text-white font-semibold py-2 rounded"
          >
            {loading ? "Processing..." : "Upload & Detect"}
          </button>
        </form>

        {transcription && (
          <div className="mt-4 text-center">
            <h2 className="font-semibold">🗣️ Transcription</h2>
            <p className="mt-2">{transcription}</p>
          </div>
        )}

        {match?.match && (
          <div className="mt-4 text-center">
            <h2 className="font-semibold">📖 Closest Match</h2>
            <p>
              Surah {match.match.surah}:{match.match.ayah}
            </p>
            <p>{match.match.arabic_text}</p>
            <p>{match.match.english_text}</p>
            <p className="text-sm">
              Confidence: {match.confidence}%
            </p>
          </div>

        )}
        </section>

        {/* FEATURES */}
      <section className="mt-12">
        <h2 className="mb-4 text-xl font-bold text-center">Features</h2>
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3">
          <div className="rounded bg-teal-400 p-4 dark:bg-teal-700 ">
            ....
          </div>
          <div className="rounded bg-teal-400 p-4 dark:bg-teal-700">
            Hifdh Game
          </div>
          <div className="rounded bg-teal-400 p-4 dark:bg-teal-700">
            Radio
          </div>
          </div>
          
      </section>
    </>
  );
}
