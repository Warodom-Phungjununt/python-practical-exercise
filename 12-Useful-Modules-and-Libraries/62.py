# สมมติรายได้และต้นทุนรายเดือนของบริษัท สคูดิโอโอโอเย่ จำกัด ในหน่วยล้านบาท ดังนี้
revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555]

# จงหาว่าแต่ละเดือนมีกำไร (หรือขาดทุน) เท่าไหร่ บันทึกใส่ตัวแปร profit
import numpy as np
revenue_arr = np.array(revenue)
cost_arr = np.array(cost)

profit = revenue_arr - cost_arr
print(profit)

# เดือนไหนกำไรหรือเท่าทุนให้ขึ้นว่า True, เดือนไหนขาดทุนให้ขึ้นว่า False
print(profit >=0)

# คำนวณอัตราส่วนกำไรต่อรายได้ บันทึกใส่ตัวแปร npm
npm = profit/revenue_arr
print(npm)

# คิดเป็น % ด้วยการคูณ 100
npm_percent = npm*100
print(npm_percent)