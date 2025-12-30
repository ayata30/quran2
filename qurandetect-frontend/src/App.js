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

    const formData = new FormData();
    formData.append("file", audioFile);


    const transcribeRes = await fetch("http://127.0.0.1:8000/transcribe", {
      method: "POST",
      body: formData,
    });

    const transcribeData = await transcribeRes.json();
    const text = transcribeData.text;
    setTranscription(text);

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
    <div className="min-h-screen flex flex-col bg-teal-100">

      {/* NAVBAR */}
      <header className="fixed top-0 left-0 w-full flex justify-between bg-teal-500 px-6 py-4 text-teal-100 z-50">
        <h1 className="text-xl font-bold">QuranDetect</h1>
        <nav className="text-md flex gap-4 ">
          <a href="#">Home</a>
          <a href="#">Calendar</a>
          <a href="#">Contact</a>
        </nav>
      </header>

      {/* MAIN CONTENT */}
      <main className="pt-20 flex-grow space-y-12 px-6">

        {/* HERO */}
        <section className="text-center">
          <h1 className="text-3xl font-bold mb-2">Detect Any Quran Recitation!</h1>

          <p className="text-md mb-4 ">
              Upload audio and instantly find the Surah & Ayah
           </p>
         </section>

        {/* DETECTION SECTION  */}
        <section className="mx-auto max-w-md rounded bg-teal-400 p-6">
          <h2 className="text-2xl font-bold mb-4 text-center">
            🎧 Try QuranDetect
          </h2>

          <input
            type="file"
            accept="audio/*"
            onChange={handleUpload}
            className="mb-4 w-full"
          />

            <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-teal-600 text-white font-semibold py-2 rounded hover:bg-teal-700 transition"
          >
            {loading ? "Processing..." : "Upload & Detect"}
          </button>
          

          {transcription && (
            <div className="mt-4 text-center">
              <h2 className="font-semibold">🗣️ Transcription</h2>
              <p className="mt-2 text-blavk-100">{transcription}</p>
            </div>
          )}

          {match?.match && (
            <div className="mt-4 text-center">
              <h2 className="font-semibold">📖 Closest Match</h2>
              <p className="mt-2 text-black-100">
                Surah {match.match.surah}:{match.match.ayah} — {match.match.text}
              </p>
              <p className="text-sm text-black-100">
                Confidence: {match.confidence}%
              </p>
            </div>
          )}
        </section>

        {/* FEATURES */}
        <section>
          <h2 className="mb-4 text-xl font-bold text-center">Features</h2>
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 hover:shadow">
            <div className="rounded bg-teal-400 p-4 hover:bg-teal-400 hover:text-teal-100">
              Detect Audio
            </div>
            <div className="rounded bg-teal-400 p-4 hover:bg-teal-400 hover:text-teal-100">
              Hifdh Game
            </div>
            <div className="rounded bg-teal-400 p-4 hover:bg-teal-400 hover:text-teal-100">
              Radio
            </div>
          </div>
        </section>

      </main>

      {/* FOOTER */}
      <footer className="bg-teal-500 text-center text-sm text-teal-100 py-2">
        © 2025 QuranDetect. All rights reserved.
      </footer>

    </div>
  );
}
