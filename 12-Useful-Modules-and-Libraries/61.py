# สมมติมี list ของส่วนสูงของสมาชิกวง Girls Generation ดังต่อไปนี้

heights = [159., 163., 158., 170., 169., 168., 162., 167., 160.]

# ลองหาวิธีคำนวณค่าเฉลี่ยของส่วนสูงสมาชิกวงนี้ โดยไม่ใช้ numpy
sum = 0
for h in heights:
    sum = sum + h

mean = sum/len(heights)
print(mean)
# ใช้วิธี numpy
import numpy as np
mean2 = np.mean(heights)
print(mean2)

# ลองหาค่ามัธยฐาน (median) ด้วย
med = np.median(heights)
print(med)