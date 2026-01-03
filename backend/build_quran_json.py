import json 

#load arabic 



quran = []
quran_arabic = {}
with open("quran-simple-plain.txt", encoding="utf-8") as f:
       for line in f:
        line = line.strip()
        if not line or "|" not in line:
            continue  # skip bad lines

        parts = line.split("|", 2)
        if len(parts) != 3:
            continue

        surah, ayah, text = parts
        quran_arabic[(int(surah), int(ayah))] = text

        quran.append({
            "surah": int(surah),
            "ayah": int(ayah),
            "text": text
        })




# Load English
quran_english = {}
with open("en.sahih.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or "|" not in line:
            continue

        parts = line.split("|", 2)
        if len(parts) != 3:
            continue

        surah, ayah, text = parts
    
        quran_english[(int(surah), int(ayah))] = text

# Combine
quran_data = []
for key in quran_arabic:
    surah, ayah = key
    quran_data.append({
        "surah": surah,
        "ayah": ayah,
        "arabic": quran_arabic[key],
        "english": quran_english.get(key, "")
    })

# Save JSON for backend use
with open("quran_full.json", "w", encoding="utf-8") as f:
    json.dump(quran_data, f, ensure_ascii=False, indent=2)



