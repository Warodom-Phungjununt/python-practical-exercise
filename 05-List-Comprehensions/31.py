# กำหนด list ของกำไร(หรือขาดทุน)รายเดือน ของบริษัท สโคดิอู้ จำกัด (มหาชน) ดังนี้ ในหน่วยพันล้านบาท
net_profits = [2574.99, -104.4, 4750.0, 1566.65, 4297.64, 3684.8, 673.09, -229.02, 624.9, -126.56, 4498.43, 2168.16]

# Ex5 : จงสร้าง list ใหม่ที่เอาเฉพาะตัวเลขที่กำไรมาอยู่ใน list ใหม่ที่ชื่อ profits
profits = [v for v in net_profits if v > 0]
print(profits)

# (Challenge) มีเดือนไหนบ้างที่ขาดทุน?
# ใส่ตัวแปร loss_months (1 = Jan, 2 = Feb, 3 = Mar, ...)
loss_months = [i+1 for i, v in enumerate(net_profits) if v < 0]
print(loss_months)