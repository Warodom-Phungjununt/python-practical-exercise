## Creating a subclass

# เราสามารถสร้าง "class ย่อย" (subclass) ที่ "ต่อยอด" (extend) มาจาก "class ต้นฉบับ" (parent class) ได้ ซึ่ง subclass จะ "รับมรดก" (inherit) attributes และ methods ต่างๆ มาจาก parent class

# Syntax:
# ```python
# class SubClassName(ParentClassName):

#     def __init__(self, parent params ..., subclass params ...):
#         super().__init__(parent params ...) #สร้าง object จากแม่พิมพ์ของ parent class
#         self.subclass_param_1 = subclass_param_1
#         self.subclass_param_2 = subclass_param_2
#         ...
# ```

# การใช้คำสั่งพิเศษ `super()` คือการเรียกใช้ parent class (อาจจะมองว่าเป็น "super class" ก็ได้ โดยที่ "super class" คือ ตรงข้ามกับ "sub class") และ `super().__init__(...)` ก็คือการเรียกใช้ method `__init__` ของ parent class นั่นเอง
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
    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.stock_quantity})"
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.stock_quantity}"
    
    def __add__(self, other):
        return (self.price * self.stock_quantity) + (other.price * other.stock_quantity)
    
# Ex35 : สร้าง class ใหม่ชื่อ Book ซึ่งเป็น subclass ของ Item
# โดยที่นอกเหนือจาก name, price, stock_quantity แล้ว
# ยังรับ parameters เพิ่มเติมคือ author (ผู้แต่ง) และ num_pages (จำนวนหน้า) ด้วย
# ให้เขียน __init__ method ของ Book class
# โดยเรียกใช้ __init__ method ของ Item class ก่อน
# แล้วค่อยเพิ่มสมบัติ author และ num_pages ตามมาทีหลัง
class Book(Item):

    def __init__(self, name, price, stock_quantity, author, num_pages):
        super().__init__(name, price, stock_quantity)
        self.author = author
        self.num_pages = num_pages

# Ex36 : สร้าง Book object สำหรับหนังสือที่มีข้อมูลดังนี้
# name = "ถ้าโลกนี้มีแต่แมวส้ม"
# price = 555
# stock_quantity = 10000
# author = "พรี่เกรท"
# num_pages = 123
# บันทึกใส่ตัวแปร book_1
# ลอง print attributes ต่างๆ ออกมาดูด้วย
item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)
book_1 = Book("ถ้าโลกนี้มีแต่แมวส้ม", 555, 10000, "พรี่เกรท", 123)
print(book_1)
print(book_1.__dict__)

# Ex37 : เพิ่ม __repr__ และ __str__ methods สำหรับ Book
# โดยไม่ต้องแคร์ว่า Item class ซึ่งเป็น parent ของ Book จะมี methods เหล่านี้อยู่แล้ว
# __repr__ ให้ผลลัพธ์เป็น Book('ชื่อหนังสือ',ราคา,จำนวนสินค้าในคลัง,'ผู้แต่ง',จำนวนหน้า)
# __str__ ให้ผลลัพธ์เป็น "Product ID: รหัสผลิตภัณฑ์, Name: ชื่อหนังสือ, Price: ราคา, Quantity: จำนวนสินค้า, Author: ผู้แต่ง, Num Pages: จำนวนหน้า"
class Book(Item):

    def __init__(self, name, price, stock_quantity, author, num_pages):
        super().__init__(name, price, stock_quantity)
        self.author = author
        self.num_pages = num_pages
    
    def __repr__(self):
        return f"Book('{self.name}',{self.price},{self.stock_quantity},'{self.author}',{self.num_pages})"
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.stock_quantity} Author: {self.author} Pages Number: {self.num_pages}"

# Ex36 : สร้าง Book object สำหรับหนังสือที่มีข้อมูลดังนี้
# name = "น่าจะรู้งี้ตั้งแต่อายุ 5 ขวบ"
# price = 20
# stock_quantity = 5
# author = "พรี่เกรท"
# num_pages = 2
# บันทึกใส่ตัวแปร book_2
# ลอง print repr(book_2) และ book_2 มาดูด้วย
book_2 = Book("น่าจะรู้งี้ตั้งแต่อายุ 5 ขวบ", 20, 5, "พรี่เกรท", 2)
print(repr(book_2))
print(book_2)

# Ex37 : สมมติว่ามีคนมาซื้อ 2 เล่ม
# ให้อัปเดตจำนวนสินค้าใน stock ด้วย
# ลองใช้ update_stock method ของ Item class ดูว่าเวิร์คไหม
# จากนั้นลอง print(book_2) ออกมาดู
book_2.update_stock(-2)
print(book_2)

# Ex38 : ลองเปลี่ยนราคาหนังสือนี้เป็น 2000 บาท
# จากนั้นลอง print(book_2) ออกมาดู
book_2.price = 2000
print(book_2)

# Ex39 : ลองใช้คำสั่ง help กับ book_2
# เพื่อดูว่ามีอะไรบ้างที่ Book class "ได้รับมรดก" (inherit) มาจาก Item class
help(book_2)

