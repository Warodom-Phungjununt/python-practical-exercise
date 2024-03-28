# กำหนด list ของกำไร(หรือขาดทุน)รายเดือน ของบริษัท สโคดิอู้ จำกัด (มหาชน) ดังนี้ ในหน่วยพันล้านบาท
net_profits = [2574.99, -104.4, 4750.0, 1566.65, 4297.64, 3684.8, 673.09, -229.02, 624.9, -126.56, 4498.43, 2168.16]

# จงสร้าง dict ที่มี key เป็นเลขเดือน และ value บอกว่าเดือนดังกล่าวกำไรหรือขาดทุน
# ถ้ากำไรหรือเท่าทุน ให้ระบุว่า "กำไร"
# ถ้าขาดทุน ให้ระบุว่า "ขาดทุน"
# บันทึกใส่ตัวแปร monthly_performance
monthly_performance = {month+1:"profit" if income>0 else "loss" for month, income in enumerate(net_profits)}
print(monthly_performance)