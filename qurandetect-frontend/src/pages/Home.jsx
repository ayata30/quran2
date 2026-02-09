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
        "https://qurandetect-backend-975745335288.us-central1.run.app/transcribe",
        {
          method: "POST",
          body: formData,
        }
      );

      const { text } = await transcribeRes.json();
    
      setTranscription(text);

      const detectRes = await fetch(
        "https://qurandetect-backend-975745335288.us-central1.run.app/detect",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({text}),
        }
      );
      const detectData = await detectRes.json();
      if (detectData.error) {
  setMatch(null);
} else {
  setMatch(detectData);
}

 
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
            accept="audio/wav,audio/mpeg,audio/mp3,audio/mp4,audio/m4a,audio/ogg"
            onChange={handleUpload}
            className="mb-4 w-full"
          />

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-teal-600 text-white font-semibold py-2 rounded dark:text-black"
          >
            {loading ? "Processing..." : "Upload & Detect"}
          </button>
        </form>
        {audioFile && (
  <audio
    controls
    className="mt-4 w-full"
    src={URL.createObjectURL(audioFile)}
  />
)}

           <div className="mt-4 rounded-lg border border-teal-600 bg-teal-200 p-4 dark:border-teal-800 dark:bg-teal-800">
  <h3 className="mb-2 text-sm font-semibold text-black-800">
    Accepted Audio Formats
  </h3>

  <ul className="list-disc pl-5 text-sm text-black-600">
    <ul>.wav (recommended)</ul>
    <ul>.mp3</ul>
    <ul>.m4a</ul>
    <ul>.ogg</ul>
  </ul>

  <p className="mt-2 text-xs text-black-800">
       Tip: For best results, upload a single ayah or three with clear recitation and minimal background noise. <p/> 
    <p> Max length: 60 seconds </p>
    <p className="mt-4 text-xs text-grey-400 text-center ">
  Note: For longer recitations, QuranDetect may return the closest matching ayah rather than the full passage.
</p>
    </p>
</div>

     
{match?.surah && (
  <div className="mt-6 max-w-2xl mx-auto bg-teal-200 rounded-xl shadow p-6 space-y-4 dark:border-teal-800 dark:bg-teal-800">
    {/* Transcription */}
    {transcription && (
      <div className="text-center">
        <h2 className="font-semibold text-lg">🗣️ Transcription</h2>
        <p className="mt-2 text-lg break-words">
          {transcription}
        </p>
      </div>
    )}

    {/* Closest Match */}
    <div className="text-center">
      <h2 className="font-semibold text-lg">📖 Closest Match</h2>

      <p className="text-gray-700 dark:text-black">
       <p> Surah {match.surah} | Ayah {match.ayah} </p>     
</p>
      <p className="text-xl leading-relaxed mt-3">
        {match.arabic}
      </p>

      {match.english && (
        <p className="italic text-purple-600 mt-2 dark:text-blue-700">
          {match.english}
        </p>
      )}

      <p className="text-sm text-gray-700 mt-2 dark:text-black">
        Confidence: {match.confidence.toFixed(2)}%
      </p>
    </div>

  </div>
)}



          

       
        </section>

        {/* FEATURES */}
      <section className="mt-12">
        <h2 className="mb-4 text-xl font-bold text-center">Features</h2>
        <h3 className="text-center mb-4 text-gray-500">Coming Soon</h3>
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3">
          <div className="rounded bg-teal-300 p-4 dark:bg-teal-700">
            Hifdh Game
          </div>
          <div className="rounded bg-teal-300 p-4 dark:bg-teal-700">
            Radio
          </div>
           
          </div>
          
      </section>
    </>
  );
}
