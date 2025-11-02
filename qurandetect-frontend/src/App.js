import Header from'./Header.jsx';  
import Footer from'./Footer.jsx';  
import Recorder from "./components/Recorder";
import React from 'react';
import './App.css';
import './index.css';
function App() {
  
  return (
    <>
     <Header />
    <div style={{ textAlign: "center", padding: "2rem" }}>
      <h1>🎙️Quran Detect</h1>
      <h3> Find verses of the Quran through QD.</h3>
      <Recorder />
    </div>
         <Footer />
    </>
  );
}

export default App;
