# กำหนดตัวแปรที่เก็บข้อความ
string1 = "APPLE"
string2 = "ORANGE"

# สร้าง Set ด้วย Set Comprehensions
vowel_letters_set = {char.lower() for char in string1 if char.lower() in string2.lower()}

# แสดงค่าออกมา
print(vowel_letters_set)

# -----------[Output]-----------

# {'e', 'a'}