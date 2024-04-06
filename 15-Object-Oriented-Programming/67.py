## Creating class methods
# ในบางสถานการณ์เราต้องการสร้าง method สำหรับ class (ไม่ใช่แค่ object ใด object หนึ่ง) จึงทำให้ต้องมีสิ่งที่เรียกว่า class method ขึ้นมา โดยสิ่งที่ต้องทำคือ เราต้อง "ปรับแต่ง" (decorate) การนิยามฟังก์ชันด้วยการใส่ "ตัวปรับแต่ง" (decorators) ว่า `@classmethod` บรรทัดเหนือการนิยามฟังก์ชัน เพื่อให้ python เข้าใจว่า นี่คือ class method ไม่ใช่ instance method ธรรมดาๆ เหมือนก่อนหน้านี้
# วิธีการใส่ decorator เป็นดังนี้
# ```python
# @classmethod
# def function_name(cls, ...):
#     cls.class_var = ...
# ```
# สังเกตอีกอย่างว่า คราวนี้ เราเปลี่ยนจาก `self` เป็น `cls` แล้ว เนื่องจากเรากำลังเข้าถึงตัว class เลย ไม่ใช่แค่ object (instance) อีกต่อไปแล้ว (จริงๆ ไม่ต้องใช้ชื่อว่า `cls` ก็ได้ แต่สากลโลกนิยมตั้งชื่อแบบนี้)

# เพิ่ม class method ชื่อ force_update_n_products
# สำหรับบังคับอัพเดต n_products ซึ่งเป็น class variable (แปลว่าไม่ใช่แค่ของ object ใด object หนึ่ง)
# โดย parameter ที่รับคือ new_n_products ซึ่งคือจำนวนผลิตภัณฑ์ใหม่ที่ต้องการ
# (สร้าง class ใหม่ทับของเดิมได้เลย)
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
    
    @classmethod
    def force_update_n_products(cls, new_n_products):
        cls.n_products = new_n_products

# สร้าง item_1 และ item_2 ใหม่จาก class Item ที่เพิ่งสร้างใหม่นี้
item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)

# สมมติว่า หลังจากนั้นมีการเพิ่ม products เข้ามาจนกระทั่งตอนนี้มีผลิตภัณฑ์ 55 รายการแล้ว
# ให้ใช้ class method force_update_n_products ในการอัปเดตให้ n_products เป็น 55
# แล้วลอง print ตัวแปร n_products ทั้งของ Item (class), item_1 และ item_2 (instance)
Item.force_update_n_products(55)
print(Item.n_products)
print(item_1.n_products)
print(item_2.n_products)

# ลอง check ว่า product_id ของ item_1 และ item_2 มีอะไรเปลี่ยนไปไหม?
print(item_1.product_id)
print(item_2.product_id)

# สร้าง item_3 ชื่อ XBOX ราคา 19000 มี 10 ชิ้นในคลัง
# จากนั้น print product_id ของ item_3
item_3 = Item('XBOX', 19000, 10)
print(item_3.product_id)

# ลอง print n_products ทั้งของ Item (class), item_1, item_2 และ item_3 (instance)
print(Item.n_products)
print(item_1.n_products)
print(item_2.n_products)
print(item_3.n_products)

# เพิ่ม class method ชื่อ from_string
# ที่รับ parameter ชื่อ product_str ซึ่งอยู่ในรูปแบบ "ชื่อผลิตภัฑณ์-ราคา-จำนวนสินค้าในคลัง"
# แล้วสร้าง object จากข้อมูลดังกล่าว
# สุดท้ายให้ return object ที่สร้างเสร็จแล้วด้วย
# (สร้าง class ใหม่ทับของเดิมได้เลย)
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
    
    @classmethod
    def force_update_n_products(cls, new_n_products):
        cls.n_products = new_n_products
    
    @classmethod
    def from_string(cls, product_str):
        name, price, stock_quantity = product_str.split("-")
        price = float(price)
        stock_quantity = int(stock_quantity)
        return cls(name, price, stock_quantity)

# สร้าง item_1 ใหม่ แต่คราวนี้สร้างจาก string "PS5-20000-5"
# จากนั้น print attributes ของ item_1 เพื่อดูผลลัพธ์
item_1 = Item.from_string('PS5-20000-5')
print(item_1)
