
import './App.css';
import { HashRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from './pages/Home';
import Radio from './pages/Radio';
import Contact from './pages/Contact';
import HifdhGame from './pages/Hifdhgame';
import PrivacyPolicy from './pages/PrivacyPolicy';
 
  
function App(){
  return(
    <Router>
    <div className="min-h-screen flex flex-col bg-teal-100 dark:bg-teal-900">

      {/* NAVBAR */}
      <header className="fixed top-0 left-0 w-full flex justify-between bg-teal-500 px-6 py-4 text-teal-100 z-50 shadow-lg dark:bg-teal-700 ">
        <h1 className="text-xl font-bold dark:text-black">QuranDetect</h1>
        <nav className="text-md flex gap-4 dark:text-black">
          <Link to="/">Home</Link>
          <Link to="/radio">Radio</Link>
           <Link to="/privacypolicy">Privacy Policy</Link>
          <Link to="/contact">Contact</Link>
          <Link to="/hifdhgame">Hifdh Game</Link>

          <button onClick={() => {
            document.documentElement.classList.toggle("dark");
          }}>Toggle Theme </button>
          
        </nav>
      </header>

      {/* MAIN CONTENT */}
      <main className="pt-20 flex-grow space-y-12 px-6">

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/radio" element={<Radio />} />
          <Route path="/privacypolicy" element={<PrivacyPolicy />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/hifdhgame" element={<HifdhGame />} />
        </Routes>
        </main>


      {/* FOOTER */}
      <footer className="bg-teal-500 text-center text-sm text-teal-100 py-2 dark:bg-teal-700 dark:text-black">
        © 2025 QuranDetect. All rights reserved. Quran text provided by Tanzil.net
  
      </footer>

    </div>
    </Router>
  );
}

export default App;