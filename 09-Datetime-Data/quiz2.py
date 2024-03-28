from datetime import datetime

# กำหนดค่าตัวแปร
NewYear2030_str = "2030-06-12"
Today_str = datetime.today().strftime("%Y-%m-%d")

date1 = datetime.strptime(NewYear2030_str, "%Y-%m-%d")
date2 = datetime.strptime(Today_str, "%Y-%m-%d")

# คำนวณจำนวนวัน
date_difference = (date1 - date2).days

# แสดงค่าออกมา
print("Difference in days:", date_difference, "days")

# -----------[Output]-----------

# Difference in days: 2267 days