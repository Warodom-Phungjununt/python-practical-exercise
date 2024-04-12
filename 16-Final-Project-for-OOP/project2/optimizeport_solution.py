# TODO: import สิ่งที่จำเป็นสำหรับโปรแกรมนี้จาก Library ชื่อ robolib
# โดยสิ่งที่ต้องการมีดังนี้
# Stock และ Portfolio classes จาก stockport
# ฟังก์ชัน read_stock_csv จาก roboutils

from robolib.stockport import Stock, Portfolio
from robolib.roboutils import read_stock_csv

if __name__ == "__main__":
    # TODO: อ่านข้อมูลหุ้นจากไฟล์ './data/faang_historical.csv'
    # โดยใช้ฟังก์ชัน read_stock_csv
    dates, historical_data = read_stock_csv('./data/faang_historical.csv')
    
    # TODO: สร้าง Portfolio object ชื่อ "MyPort" ใส่ตัวแปร port
    port = Portfolio("MyPort")

    # TODO: จาก historical_data (Hint: อ่าน docstring ของฟังก์ชัน read_stock_csv)
    # ให้สร้าง Stock object ของหุ้นแต่ละตัว
    # จากนั้นเพิ่มมันเข้าไปใน port ของเรา
    for name, historical_prices in historical_data.items():
        stock = Stock(name, historical_prices)
        port.add_stock(stock)

    # TODO: print แสดงผลลัพธ์ว่าใน port ของเรามีหุ้นอะไรอยู่บ้าง
    port.print_stocks()
    
    # TODO: เขียนโค้ดรับ input จากผู้ใช้ ว่าต้องการผลตอบแทนเป้าหมายรายวันเท่าใดระหว่าง 0%-100%
    # จากนั้นอย่าลืมเปลี่ยนให้เป็นตัวเลขระหว่าง 0-1 (ไม่ใช่ 0-100 นะ!!!)
    # บันทึกผลลัพธ์ใส่ตัวแปร target_daily_return
    target_daily_return = input("Enter your target daily return (0-100): ")
    target_daily_return = float(target_daily_return)/100

    # TODO: ใช้ method ชื่อ cal_optimized_weights
    # เพื่อคำนวณหาน้ำหนักของหุ้นแต่ละตัวที่ให้ผลตอบแทนที่ต้องการด้วยความเสี่ยงต่ำที่สุด
    port.cal_optimized_weights(target_daily_return)

    # TODO: ใช้ method ชื่อ cal_expected_yearly_returns
    # เพื่อคำนวณหาว่าสุดท้ายแล้วพอร์ตของเรา ให้ผลตอบแทนต่อปีเป็นเท่าใด
    # และ print แสดงผลลัพธ์ด้วย อย่าลืมตั้งค่าให้ print ออกมาเป็น %
    expected_yearly_return = port.cal_expected_yearly_returns()
    print("Expected yearly return is {:.2%}".format(expected_yearly_return))

    # TODO: ให้ลองลบหุ้น 'goog' ออกจาก port ของเรา
    # แล้วคำนวณน้ำหนักใหม่อีกรอบ โดยใช้ผลตอบแทนที่ต้องการตามเดิม
    port.remove_stock('goog')
    port.cal_optimized_weights(target_daily_return)