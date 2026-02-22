'''
import sqlite3
import json

# 1. Load the JSON
with open("quran_full.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Connect to SQLite
conn = sqlite3.connect("quran1.db")
cursor = conn.cursor()

# 3. Create table with an English column
'''
cursor.execute('''CREATE TABLE IF NOT EXISTS verses 
                  (id INTEGER PRIMARY KEY, 
                   surah INTEGER, 
                   ayah INTEGER, 
                   arabic TEXT, 
                   english TEXT, 
                   normalized TEXT)''')
''''
# 4. Insert data
for v in data:
    # Basic normalization (stripping accents)
    # You can swap this for your full normalize_arabic function
    norm = v["arabic"].replace(" ", "") 
    
    cursor.execute("""INSERT INTO verses (surah, ayah, arabic, english, normalized) 
                      VALUES (?, ?, ?, ?, ?)""", 
                   (v["surah"], v["ayah"], v["arabic"], v.get("english", ""), norm))

conn.commit()
conn.close()
print("Success! quran.db now includes English text.")
'''