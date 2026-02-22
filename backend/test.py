
import json
from utils.fuzzy_match import match_verse

# Load Quran JSON
with open("quran_full.json", "r", encoding="utf-8") as f:
    quran_db = json.load(f)

# Example fuzzy test transcripts (simulate Google Speech API)
test_transcripts = [
    "بسم الله الرحمن الرحيم",                 # Exact
    "وَأَنَّا مِنَّا الصَّالِحُونَ وَمِنَّا دُونَ ذَٰلِكَ كُنَّا طَرَائِقَ قِدَدًا", # Exact
    "بسم الله الرحمٰن الرحيم",  
                 "حمد لله رب",
    "قل هو الله احد",
    "هذا نص عشوائي"             # Slight variation
]

for transcript in test_transcripts:
    matched = match_verse(transcript, quran_db, threshold=70)

    print("Transcript:", transcript)

    if matched:
        print(
            f"Matched → Surah {matched['surah']} | Ayah {matched['ayah']} "
            f"| Confidence: {matched['confidence']}"
        )
        print("Arabic:", matched["arabic"])
        
       # print("English:", matched["english"])   
    else:
        print("No confident match")

    print("-" * 40)
    print("Best score:", score)
print("Matched text:", match_text)



