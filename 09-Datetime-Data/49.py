import datetime as dt
# กำหนดข้อความแสดงวันเกิดของน้อง Hanni ซึ่งเกิดวันที่ 6 ตุลาคม 2004 ดังนี้
hanni_bd_str = "06/10/2004 17:30:22"
bd_format = "%d/%m/%Y %H:%M:%S"

# จงสร้าง datetime object ชื่อ hanni_bd_dt
# ที่มีค่าเป็นวันเวลาเกิดของน้อง Hanni
# print แสดงผลลัพธ์ออกมาด้วย
# พร้อมทั้ง print ประเภทข้อมูลของตัวแปร hanni_bd_dt
hanni_bd_dt = dt.datetime.strptime(hanni_bd_str, bd_format)
print(hanni_bd_dt)
print(type(hanni_bd_dt))