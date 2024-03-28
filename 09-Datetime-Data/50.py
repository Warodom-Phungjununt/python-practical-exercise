# จากตัวแปร hanni_bd_dt ในตัวอย่างที่แล้ว
import datetime as dt
hanni_bd_str = "06/10/2004 17:30:22"
bd_format = "%d/%m/%Y %H:%M:%S"
hanni_bd_dt = dt.datetime.strptime(hanni_bd_str, bd_format)

# จงแสดงออกมาเป็นข้อความที่มีรูปแบบดังนี้
# วันของสัปดาห์แบบย่อ, เดือนเต็ม วันที่, ปี ค.ศ.
# บันทึกใส่ตัวแปร hanni_bd_usa
# print แสดงผลลัพธ์ออกมา
# พร้อมทั้ง print ประเภทข้อมูลของตัวแปร hanni_bd_usa ด้วย
hanni_bd_usa = hanni_bd_dt.strftime("%a, %B %d, %Y")
print(hanni_bd_usa)
print(type(hanni_bd_usa))

# Note: ถ้าไม่อยากให้มีเลข 0 นำหน้าวันที่ 06 ใช้โค้ดลับ %-d ได้
hanni_bd_usa_2 = hanni_bd_dt.strftime("%a, %B %-d, %Y")
print(hanni_bd_usa_2)
print(type(hanni_bd_usa_2))