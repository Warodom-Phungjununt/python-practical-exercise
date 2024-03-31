import random
# ลองวนลูปสร้างเลขสุ่มระหว่าง -5 กับ 5
# 10 ครั้ง โดยยัดค่าใส่ list ที่ชื่อ random_list2
random_list2 = [random.uniform(-5, 5) for i in range (10)]
print(random_list2)