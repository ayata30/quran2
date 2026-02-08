# utils/fuzzy_match.py

import re
from rapidfuzz import fuzz, process

def normalize_arabic(text):
    text = re.sub(r'[ًٌٍَُِّْ]', '', text)
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    text = text.replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي")
    text = text.replace("ة", "ه")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def match_verse(transcript, quran_db, threshold=70):
    transcript_norm = normalize_arabic(transcript)
    if len(transcript_norm) < 5:
        return None
# normlaize qurna text
    normalized_verses = [
        normalize_arabic(v["arabic"]) for v in quran_db
    ]
    #matchnig 
    match_text, score, index = process.extractOne(
        transcript_norm,
        normalized_verses,
        scorer=fuzz.partial_ratio

    )
    if score < threshold:
        return None
    
    result = quran_db[index].copy()
    result["confidence"] = score
    return result

  