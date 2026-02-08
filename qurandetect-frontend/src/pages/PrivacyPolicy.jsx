export default function PrivacyPolicy() {
    return (
        <div>
        <h2 className="text-2xl font-bold">Privacy Policy </h2>

       <h3 className="text-sm text-gray-500 font-semibold"> Privacy Policy – QuranDetect (QD) </h3>

       <p className="text-sm text-gray-500 font-semibold"> Last updated: February 2026 </p>  
    <p> 
      QuranDetect (“QD”, “we”, “our”, or “us”) respects your privacy.
     This Privacy Policy explains how we handle information when you use our application. 

   </p>

<h4 className="font-semibold mt-4"> 1. Information We Collect  </h4>

<p> QuranDetect is designed to be privacy-focused. We collect minimal data, only what is necessary for the app to function.
    </p>

<h4 className="font-semibold mt-4">2. How We Use Your Data  </h4>
<p> <strong>Audio recordings:</strong> When you upload or record audio, it is used solely to:
transcribe the recitation and identify the matching Surah and Ayah. </p>
<p> <strong>Transcribed text:</strong> The transcription generated from audio is used temporarily to match verses from the Quran. </p>

<h4 className="font-semibold mt-4">3. We do not collect: </h4>
     <ul className="list-disc ml-6 space-y-1">
        <li>Names, emails, or account information</li>
        <li>Location data</li>
        <li>Device identifiers</li>
        <li>Browsing history</li>
      </ul>
      <p>
        Audio files and transcriptions are processed temporarily and are not stored permanently.
      </p>

      <h4 className="font-semibold mt-4">4. Data Storage and Retention</h4>

      <ul className="list-disc ml-6 space-y-1">
        <li>Audio files are processed in memory or temporary storage</li>
        <li>No audio recordings or transcriptions are retained after processing</li>
        <li>No user data is stored for tracking or analytics purposes</li>
      </ul>

      <h4 className="font-semibold mt-4">5. Third-Party Services</h4>

      <p>
        QuranDetect may use third-party APIs or machine learning services
        (such as speech-to-text services) solely to perform transcription.
        These services process data in accordance with their own privacy policies.
        QuranDetect does not sell or share user data.
      </p>

      <h4 className="font-semibold mt-4">6. Data Security</h4>

      <p>
        Audio and text data are transmitted to backend endpoints solely for
        temporary processing and are not stored.
      </p>

      <p className="text-sm text-gray-500">
        No system is completely secure, and we cannot guarantee absolute security.
      </p>

      <h4 className="font-semibold mt-4">7. Children’s Privacy</h4>

      <p>
        QuranDetect does not knowingly collect personal information from children under 13.
      </p>

      <h4 className="font-semibold mt-4">8. Changes to This Policy</h4>

      <p>
        We may update this Privacy Policy as the app evolves. Updates will be
        reflected on this page with a revised “Last updated” date.
      </p>

      <h4 className="font-semibold mt-4">9. Contact</h4>

      <p>
        If you have questions about this Privacy Policy, you may contact us
        through the project repository or application page.
      </p>

           
        </div>
    );
}