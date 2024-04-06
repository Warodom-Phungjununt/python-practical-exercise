# Creatine Instance Method
# instance methods = คำสั่งของแต่ละ object
# เพิ่ม method ชื่อ update_stock ที่มีหน้าที่อัปเดตจำนวนสินค้าในคลัง
# โดยรับ parameter ชื่อ quantity ซึ่งคือจำนวนสินค้าที่เพิ่มขึ้น (หรือลดลงถ้าติดลบ)
# (Optional) หากตอนใช้ method ไม่ระบุ quantity ให้ตั้งค่า default เป็น -1
# (ให้สร้าง class Item ใหม่ ทับของเดิมได้เลย)

class Item():
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    def update_stock(self, quantity = -1):
        self.stock_quantity += quantity

# สมมติสถานการณ์ว่า มีคนมาซื้อ PS5 ทั้งสิ้น 2 เครื่อง
# ให้อัปเดตจำนวนสินค้าในคลังให้ถูกต้องด้วย method update_stock
# (ให้สร้าง item_1 ใหม่ด้วย class ที่สร้างใหม่นี้ ทับของเดิมได้เลย)
item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)
item_1.update_stock(-2)
print(item_1.name)
print(item_1.price)
print(item_1.stock_quantity)

# สมมติสถานการณ์ว่า มีคนมาซื้อ PS5 เพิ่มอีก 1 เครื่อง
# ให้อัปเดตจำนวนสินค้าในคลังให้ถูกต้องด้วย method update_stock
item_1.update_stock()
print(item_1.name)
print(item_1.price)
print(item_1.stock_quantity)

# สมมติสถานการณ์ว่า มีคนมาซื้อ Nintendo Switch ทั้งสิ้น 2 เครื่อง
# ให้อัปเดตจำนวนสินค้าในคลังให้ถูกต้องด้วย method update_stock
# แต่ให้เรียกใช้ method นี้ด้วยวิธี Item.update_stock(...)
# (ให้สร้าง item_2 ใหม่ด้วย class ที่สร้างใหม่นี้ ทับของเดิมได้เลย)
item_2.update_stock(-2)
print(item_2.name)
print(item_2.price)
print(item_2.stock_quantity)
Item.update_stock(item_2,-2)
print(item_2.name)
print(item_2.price)
print(item_2.stock_quantity)

# สมมติ เติม stock 50 ชิ้น
Item.update_stock(item_1,50)
Item.update_stock(item_2,50)
print(item_1.name)
print(item_1.price)
print(item_1.stock_quantity)
print(item_2.name)
print(item_2.price)
print(item_2.stock_quantity)