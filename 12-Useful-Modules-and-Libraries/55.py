import random
# ลองวนลูปสร้าง**จำนวนเต็ม**สุ่มระหว่าง 0 ถึง 100
# 10 ครั้ง โดยยัดค่าใส่ list ที่ชื่อ random_list3
random_list3 = [random.randrange(101) for i in range(10)]
print(random_list3)

# ลองวนลูปสร้าง**จำนวนเต็ม**สุ่มระหว่าง -5 ถึง 5
# 10 ครั้ง โดยยัดค่าใส่ list ที่ชื่อ random_list4
random_list4 = [random.randrange(-5, 6) for i in range(10)]
print(random_list4)