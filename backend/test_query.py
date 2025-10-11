import sqlite3

conn = sqlite3.connect("quran_detect.db")
cursor = conn.cursor()

cursor.execute("SELECT surah_name_en, ayah_number, ayah_text_en FROM quran WHERE surah_number=1")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
