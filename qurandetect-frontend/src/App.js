
import './App.css';
import { HashRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from './pages/Home';
import Radio from './pages/Radio';
import Contact from './pages/Contact';
import HifdhGame from './pages/Hifdhgame';
import PrivacyPolicy from './pages/PrivacyPolicy';
import { useEffect } from "react";
 
  
function App(){

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme") ;
    if ( savedTheme === "dark" ){
       document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, []);
    
  return(
    <Router>
    <div className="min-h-screen flex flex-col bg-teal-100 dark:bg-teal-900">

      {/* NAVBAR */}
      <header className="fixed top-0 left-0 w-full bg-teal-500 px-4 sm:px-6 py-3 text-teal-100 z-50 shadow-lg dark:bg-teal-700 ">
        <div className="flex flex col sm:flex-row sm:justify-between sm:items-center gap-2"> 
         
        <h1 className="font-bold text-2xl sm:text-2xl dark:text-black">
           <Link to="/" clasName="hover:opacity-80 transition">
           QuranDetect
           </Link>
          </h1>
        
        <nav className="flex flex-wrap gap-3 text-sm: sm:text-md dark:text-black">
          <Link to="/" className="hover:opacity-80 transition dark:hover:opacity-70 transition">
          Home</Link>
          <Link to="/radio" className="hover:opacity-80 transition"
          >Radio</Link>
           <Link to="/privacypolicy" className="hover:opacity-80 transition">Privacy Policy</Link>
          <Link to="/contact" className="hover:opacity-80 transition">Contact</Link>
          <Link to="/hifdhgame" className="hover:opacity-80 transition">Hifdh Game</Link>

          <button
             className="hover:opacity-80 transition"
           onClick={() => {
            const isDark = document.documentElement.classList.toggle("dark");
            if (isDark){
              localStorage.setItem("theme","dark");
            } else{
              localStorage.setItem("theme", "light");
            }
          }}>Toggle Theme </button>
          
        </nav>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="pt-28 flex-grow space-y-12 px-6">

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/radio" element={<Radio />} />
          <Route path="/privacypolicy" element={<PrivacyPolicy />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/hifdhgame" element={<HifdhGame />} />
        </Routes>
        </main>


      {/* FOOTER */}
      <footer className="w-full bg-teal-500 text-center text-sm text-teal-100 py-2 mx-auto mt-auto dark:bg-teal-700 dark:text-black">
        <p>©2025 QuranDetect. All rights reserved. Quran text provided by Tanzil.net</p>
      </footer>
    </div>
    </Router>
  );
}

export default App;