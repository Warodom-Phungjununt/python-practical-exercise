import datetime as dt
# สร้างตัวแปรวันเกิดของคุณเองใส่ตัวแปร my_bd
# และตัวแปร today ที่เป็นวันที่ ณ ปัจจุบัน
# จากนั้น หาคำนวณอายุของคุณใส่ตัวแปร my_age ให้มีผลลัพธ์เป็นหน่วยวัน
# print แสดงผลลัพธ์ด้วย
my_bd = dt.date(1995, 9, 23)
today = dt.date.today()
print(today)
my_age = today - my_bd
print(my_age)

# จงหาวิธีในการดึงเอาข้อมูล ปี, เดือน, วัน
# ของ today มา บันทึกใส่ตัวแปร y, m และ d ตามลำดับ
# ข้อมูล year, month, day เป็นสมบัติ (Attribute) ของ Object
y = today.year
m = today.month
d = today.day
print(y, m, d)

# จงสร้างตัวแปรชื่อ right_now
# ที่เป็น วัน เดือน ปี และเวลา ปัจจุบัน
# print แสดงผลลัพธ์ด้วย
# Hint : เราสามารถใช้ method ชื่อ .now()
# ที่เป็น method สำหรับข้อมูลประเภท datetime ได้
right_now = dt.datetime.now(tz = dt.timezone(dt.timedelta(hours = 7)))
print(right_now)

# หมอดูทำนายว่า อีก 36 วัน กับอีก 4 นาที
# นับจากการกด run cell เมื่อกี๊
# คุณจะพบกับเนื้อคู่ จงหาว่า วันนั้นคือวัน และเวลาใด
# บันทึกใส่ตัวแปร meet_soulmate
# และ print แสดงผลลัพธ์ด้วย
meet_soulmate = right_now + dt.timedelta(days = 36, minutes = 4)
print(meet_soulmate)

# หมอดูบอกอีกว่า ก่อนหน้าจะ meet_soulmate
# เป็นเวลา 55 วินาทีเป๊ะ คุณกำลังนั่งปลดทุกข์ก้อนสุดท้ายอยู่
# จงหาว่าจังหวะปลดทุกข์ก้อนสุดท้ายคือวันเวลาใด
# บันทึกใส่ตัวแปร last_poop
# และ print แสดงผลลัพธ์ด้วย
last_poop = meet_soulmate - dt.timedelta(seconds = 55)
print(last_poop)