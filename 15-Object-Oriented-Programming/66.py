## Class variables vs. Instance variables
# Class variable = ตัวแปรของ class ที่ทุก object ใช้ร่วมกัน
# Instance variable = attribute (สมบัติ) ของแต่ละ object นั่นคือแต่ละ object มีค่าของตัวเอง ไม่ใช่ร่วมกัน

# เพิ่ม class variable ชื่อ n_products ซึ่งคือจำนวนชนิดผลิตภัณฑ์ทั้งหมดที่มี
# และเพิ่ม attribute ชื่อ product_id ที่มีรูปแบบ P-XXXXXX โดย XXXXXX คือเลข 6 หลัก
# สำหรับสินค้าแรกที่ถูกสร้าง จะมี product_id เป็น P-000001
# และสินค้าที่สองเป็น P-000002 เป็นเช่นนี้ไปเรื่อยๆ
# กล่าวคือ เราสร้าง product_id ได้จาก n_products ที่มีในปัจจุบัน
# (ให้สร้าง class Item ใหม่ ทับของเดิมได้เลย)
class Item():
    n_products = 0
    def __init__(self, name, price, stock_quantity):
        # When init is used, n_product is added.
        Item.n_products += 1
        self.product_id = "P-{:06}".format(Item.n_products) # Start with 0 and this code is 6 digits
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    def update_stock(self, quantity = -1):
        self.stock_quantity += quantity

# ลองสร้าง item_1 (PS5) ใหม่ด้วย class ที่สร้างขึ้นมาใหม่นี้
# ลองดูว่าเรา print item_1.n_products ได้หรือไม่
# แล้วลอง print attributes ต่างๆ ที่มีของ item_1 ดูด้วย
item_1 = Item('PS5', 20000, 5)
print(item_1.n_products)
print(item_1.__dict__)


# ลองสร้าง item_2 (Nintendo Switch) ใหม่ด้วย class ที่สร้างขึ้นมาใหม่นี้
# ลองดูว่าเรา print item_2.n_products ได้หรือไม่
# แล้วลอง print attributes ต่างๆ ที่มีของ item_2
item_2 = Item('Nintentendo Switch', 15000, 10)
print(item_2.n_products)
print(item_2.__dict__)

# ลอง print ว่า n_products ของ object item_1 มีค่าเป็นเท่าไหร่?
# เราจะตีความจากผลลัพธ์ตรงนี้ได้ว่าอย่างไร?
print(item_1.n_products)

# ลองใช้คำสั่ง help กับ item_1 เพื่อดูข้อมูลต่างๆ ของ item_1
# help(item_1)

# เพิ่ม class variable ชื่อ owner โดยมีค่าเริ่มต้นเป็น "Skooldio"
# (สร้าง class ใหม่ทับของเดิมเลย)
class Item():
    n_products = 0
    owner = 'Skooldio'
    def __init__(self, name, price, stock_quantity):
        # When init is used, n_product is added.
        Item.n_products += 1
        self.product_id = "P-{:06}".format(Item.n_products) # Start with 0 and this code is 6 digits
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    def update_stock(self, quantity = -1):
        self.stock_quantity += quantity

# สร้าง item_1 (PS5) ขึ้นมาใหม่ด้วย class ที่เพิ่งสร้างใหม่นี้
# ลอง print attribute ชื่อ owner ของ item_1 (item_1.owner) ดูว่าได้ไหม
# และลอง print instance variables (attributes) ของ item_1 มาดูด้วยว่ามีอะไรบ้าง
item_1 = Item('PS5', 20000, 5)
print(item_1.owner)
print(item_1.__dict__)

# สร้าง item_2 (Nintendo Switch) ขึ้นมาใหม่ด้วย class ที่เพิ่งสร้างใหม่นี้
# ลอง print attribute ชื่อ owner ของ item_2 ดูว่าเป็นอย่างไร
# ลอง print instance variables ของ item_2 มาดูด้วยว่ามีอะไรบ้าง
item_2 = Item('Nintentendo Switch', 15000, 10)
print(item_2.owner)
print(item_2.__dict__)

# จากนั้น ลอง "เปลี่ยน" owner ของ item_2 เป็น "Great"
# แล้วลอง print attribute ชื่อ owner ของ item_2 ดูอีกรอบว่าเป็นอย่างไร
# สุดท้ายลอง print instance variables ของ item_2 มาดูด้วยว่ามีอะไรบ้าง
# เราจะตีความผลลัพธ์นี้ว่าอย่างไร?
item_2.owner = 'Great' # When you change the class variable
print(item_1.owner)
print(item_2.owner)
print(item_1.__dict__)
print(item_2.__dict__) # There will be a new instance named owner in the class

# ลองใช้คำสั่ง help กับ item_2 เพื่อดูว่าการตีความในข้อที่แล้ว make sense หรือไม่
