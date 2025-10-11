import React, { useState, useRef } from "react";

function Recorder() {
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState("");
  const mediaRecorder = useRef(null);
  const audioChunks = useRef([]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder.current = new MediaRecorder(stream);

      mediaRecorder.current.ondataavailable = (event) => {
        audioChunks.current.push(event.data);
      };

      mediaRecorder.current.onstop = () => {
        const blob = new Blob(audioChunks.current, { type: "audio/wav" });
        audioChunks.current = [];
        const url = URL.createObjectURL(blob);
        setAudioURL(url);
      };

      mediaRecorder.current.start();
      setRecording(true);
    } catch (err) {
      console.error("Error accessing microphone:", err);
    }
  };

  const stopRecording = () => {
    mediaRecorder.current.stop();
    setRecording(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <h2>🎙️ QuranDetect Recorder</h2>
      <button onClick={recording ? stopRecording : startRecording}>
        {recording ? "Stop Recording" : "Start Recording"}
      </button>
      {audioURL && (
        <div style={{ marginTop: "1rem" }}>
          <p>Preview your recording:</p>
          <audio controls src={audioURL}></audio>
        </div>
      )}
    </div>
  );
}

export default Recorder;
