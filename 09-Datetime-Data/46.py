# ลองสร้างตัวแปร hanni_bd ที่มีข้อมูลวันเดือนปีเกิดของน้อง Hanni (6 OCT 2004) ในรูปแบบ date
# จงสร้างให้สำเร็จ ด้วยวิธีการใดก็ได้ที่ได้เรียนมา
# และ print แสดงค่าของตัวแปรและประเภทของข้อมูลออกมาดูด้วย
## วิธีที่ 1 (import มาทั้งโมดูล)
import datetime
thedome_bd1 = datetime.date(1995, 9, 23)
print(f"The Dome birthday type 1 is {thedome_bd1}")

## วิธีที่ 2 (import มาทั้งโมดูล แล้วตั้งชื่อย่อ)
import datetime as dt
thedome_bd2 = dt.date(1995, 9, 23)
print(f"The Dome birthday type 2 is {thedome_bd2}")

## วิธีที่ 3 (import ไส้ในของ module มาใช้)
from datetime import date
thedome_bd3 = date(1995, 9, 23)
print(f"The Dome birthday type 3 is {thedome_bd3}")