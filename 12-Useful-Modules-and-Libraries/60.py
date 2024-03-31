# เนื่องจากเรายังไม่ได้เล่นกับข้อมูลขนาดใหญ่ๆ หรือเขียนโปรแกรมที่ซับซ้อน
# จนถึงขั้นทำให้การประมวลผลใช้เวลานาน
# เราจะ "จำลอง" การ "รอนาน" ด้วยการสั่งให้โปรแกรม "หลับ" ระหว่างทำงาน
# ซึ่งสามารถทำได้ดังนี้

import time
import random

from tqdm import tqdm

print('Begin sleeping')
time.sleep(2) #หลับนาน 2 วินาที
print('Awake!')

# วนลูปทอดลูกเต๋า 1 ลูก ทั้งหมด 10 ครั้ง แต่ละครั้งให้รอนานระหว่าง 0.5 - 3 วินาที
# บันทึกผลการทอดแต่ละครั้งใส่ตัวแปร toss_results
# และใช้ tqdm ในการดู progress การรันโปรแกรม

dice_sides = [1,2,3,4,5,6]
toss_results = []
for i in tqdm(range(10)):
    side = random.choice(dice_sides)
    toss_results.append(side)
    sleep_time = random.uniform(0.5, 3)
    time.sleep(sleep_time)

print(toss_results)