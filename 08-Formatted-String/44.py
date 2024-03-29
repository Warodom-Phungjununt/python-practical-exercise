# กำหนดค่ารายได้ในหน่วยดอลล่าร์ดังนี้
revenue_usd = 123456789.23
# สมมติกำหนดอัตราแลกเปลี่ยนดังนี้ (1 USD = 35.71 THB)
usd_to_thb = 35.71
# ใช้วิธี .format() แสดงผลลัพธ์รายได้ในหน่วยบาท
# โดยให้แสดงผลเป็นทศนิยม 2 ตำแหน่ง
# print ข้อความออกมาดังนี้
# "รายได้ของบริษัทเราคือ ___________ บาท"
print(f"รายได้ของบริษัทเราคือ {revenue_usd*usd_to_thb} บาท")

# (Bonus) จงแสดงผลลัพธ์แบบให้มีเครื่องหมาย , คั่นทุกๆ หลักพัน
# เพื่อให้อ่านง่าย
print("รายได้ของบริษัทเราคือ {:,.2f} บาท".format(revenue_usd*usd_to_thb))