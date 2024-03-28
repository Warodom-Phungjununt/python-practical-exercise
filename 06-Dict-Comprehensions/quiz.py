# กำหนด Dict ที่ต้องการจะแปลง
number_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# สร้าง Dict โดยใช้ Dict Comprehensions
squared_dict = {index: val**2 for index, val in number_dict.items()}

# แสดงค่าออกมา
print(squared_dict)

# -----------[Output]-----------

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}