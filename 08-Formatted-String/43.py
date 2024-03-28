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

# จง print ชื่อ นามสกุล และอายุของนักวิทย์แต่ละคน
# คนละบรรทัด ในรูปแบบต่อไปนี้
# Name: _________ | Birth: _____
# ใช้วิธี f-string
for name, birth in scientists.items():
    print(f"Name: {name} | Birth: {birth}")

# ใช้วิธี .format()
for name, birth in scientists.items():
    print("Name: {} | Birth: {}".format(name, birth))

# จากตัวอย่างเมื่อสักครู จัดการแสดงผลให้มีการเรียงตัวสวยกว่านี้
# โดยให้ชื่อ นามสกุล และปีเกิด แต่ละอย่างขึ้นต้นอยู่ในแนวดิ่งเดียวกัน
# ใช้วิธี f-string
for name, birth in scientists.items():
    print(f"Name: {name:20} | Birth: {birth}")

# ใช้วิธี .format()
for name, birth in scientists.items():
    print("Name: {:20} | Birth: {}".format(name, birth))

