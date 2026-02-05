# utils/fuzzy_match.py

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
    arabic_texts = [normalize_arabic(v["arabic"]) for v in quran_db]

    match, score, index = process.extractOne(
        transcript_norm, arabic_texts, scorer=fuzz.ratio
    )
    best_match = None
    best_score = 0
    for verse in quran_db:
        score = fuzz.ratio(transcript, verse["arabic"])
    return best_match

    if score >= threshold:
        return quran_db[index]
    return None 
  


