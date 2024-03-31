import pandas as pd

# อ่านไฟล์ employees.csv ที่อยู่ในโฟลเดอร์ data
df = pd.read_csv("./employees.csv")

# แสดง 10 แถวแรกของตาราง
first_10_rows = df.head(10)
print(first_10_rows)

# print จำนวนแถวและจำนวนคอลัมน์ของ df ออกมาดู
print(df.shape)

# หาค่าเฉลี่ยและผลรวมของ salary
# print แสดงผลลัพธ์ให้อ่านง่ายๆ ด้วย
mean_salary = df["salary"].mean()
total_salary = df["salary"].sum()
print(f"Mean salary is {mean_salary}")
print(total_salary)
# บริษัทนี้มีคนแต่งงานแล้วกี่คน
print(df["is_married"].sum())

# บริษัทนี้ มีพนักงานชายและหญิงอย่างละกี่คน
print(df["gender"].value_counts())

# มีใครบ้างที่เงินเดือนเกิน 70000
print(df[df['salary']>70000])

# ค่าเฉลี่ยเงินเดือนแบ่งตาม gender เป็นอย่างไร?
print(df.groupby('gender')['salary'].mean())