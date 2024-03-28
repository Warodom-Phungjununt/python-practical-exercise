# กำหนด dict ของชื่อและปีเกิดนักวิทยาศาสตร์ดังนี้
scientists = {
    "Albert Einstein": 1879,
    "Isaac Newton": 1643,
    "Marie Curie": 1867,
    "Galileo Galilei": 1564,
    "Nikola Tesla": 1856,
    "Charles Darwin": 1809,
    "Thomas Edison": 1847,
    "Stephen Hawking": 1942,
    "Richard Feynman": 1918,
    "Max Planck": 1858,
    "Carl Sagan": 1934,
    "Louis Pasteur": 1822,
    "Niels Bohr": 1885,
    "Sigmund Freud": 1856,
    "Johannes Kepler": 1571,
    "Ada Lovelace": 1815,
    "Rosalind Franklin": 1920,
    "James Watson": 1928,
    "Francis Crick": 1916,
    "Alexander Fleming": 1881
}

# จงสร้าง dict ของนักวิทยาศาสตร์ที่คำนวณอายุ ณ ปัจจุบันถ้าเขายังมีชีวิตอยู่ในปี 2024
# (ไม่ต้องซีเรียสเรื่องเดือน)
# key = ชื่อนักวิทย์, value = อายุ (ปี)
# บันทึกใส่ตัวแปร scientists_age
scientists_age = {name: 2024-year for name, year in scientists.items()}
print(scientists_age)