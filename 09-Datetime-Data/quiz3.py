from datetime import datetime, timedelta

# กำหนดค่าตัวแปร
birthdate_str = "1995-09-23"
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

current_date = datetime.now()

next_birthday = datetime(current_date.year, birthdate.month, birthdate.day)
if next_birthday < current_date:
    next_birthday = datetime(current_date.year + 1, birthdate.month, birthdate.day)

days_until_birthday = (next_birthday - current_date).days

# แสดงค่าออกมา
print("Days until your next birthday:", days_until_birthday, "days")

# -----------[Output]-----------

# Days until your next birthday: 178 days