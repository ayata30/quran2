import sqlite3

conn = sqlite3.connect("quran_detect.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quran (
    id INTEGER PRIMARY KEY,
    surah_number INT,
    ayah_number INT,
    ayah_text_ar TEXT,
    ayah_text_en TEXT,
    surah_name_ar TEXT,
    surah_name_en TEXT
);
""")


# insert mock data (Al-Fatiha: 1:1)
cursor.execute("""
INSERT INTO quran (surah_number, ayah_number, ayah_text_ar, ayah_text_en, surah_name_ar, surah_name_en)
VALUES (1, 1, 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
        'In the name of Allah, the Entirely Merciful, the Especially Merciful',
        'الفاتحة', 'Al-Fatiha');
""")

conn.commit()
conn.close()

print("✅ Database initialized and mock data inserted!")