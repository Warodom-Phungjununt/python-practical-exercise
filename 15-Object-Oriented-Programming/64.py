# Creating a Class and its Instance
# สร้าง class ชื่อ Item
# โดยแต่ละ Item object จะมีสมบัติ (Attributes) เบื้องต้น คือ
# name = ชื่อสินค้า
# price = ราคาสินค้า (สมมติเป็นหน่วยบาท)
# stock_quantity = จำนวนชิ้นที่มีในคลัง

class Item():
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

# ลองสร้าง Item objects 2 อัน
# item_1 คือ PS5 ราคา 20000 บาท มี 5 ชิ้น
# item_2 คือ Nintendo Switch ราคา 15000 บาท มี 10 ชิ้น
# ลอง print ผลลัพธ์ออกมาดูด้วย

item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)

print(item_1)
print(item_2)

# ลอง print ชื่อสินค้า ราคา และ จำนวนสินค้นในคลังของ item_1
print(item_1.name)
print(item_1.price)
print(item_1.stock_quantity)

# ลองเปลี่ยนราคาสินค้าของ item_1 เป็น 18000
item_1 = Item('PS5',18000, 5)
print(item_1.name)
print(item_1.price)
print(item_1.stock_quantity)