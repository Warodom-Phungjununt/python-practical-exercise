import random
# ลองวนลูปสร้างเลขสุ่มระหว่าง 0 กับ 1
# 10 ครั้ง โดยยัดค่าใส่ list ที่ชื่อ random_list
random_list = [random.random() for i in range(10)]
print(random_list)