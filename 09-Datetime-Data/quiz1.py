from datetime import datetime, timedelta

# วันที่ปัจจุบัน
current_date = datetime.now()

# คำนวณ 23 ปี ต่อจากนี้
new_planet_date = current_date + timedelta(days=23 * 365)

# แสดงค่าออกมา
print("Earthlings will move to a new planet on:", new_planet_date.strftime("%Y-%m-%d"))

# -----------[Output]-----------

# Earthlings will move to a new planet on: 2047-03-23