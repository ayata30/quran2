import json

input_file = "C:/Users/ayata/Downloads/quran-simple-plain.txt"
#"C:\Users\ayata\Downloads\quran-simple-plain.txt"
output_file = "quran.json"


data = []
# storing each verse as a dictorinay 'surah, ayah, text'

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue

        surah, ayah, text = parts
        data.append({
            "surah": int(surah),
            "ayah": int(ayah),
            "text": text
})

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(data)} ayahs to {output_file}")



