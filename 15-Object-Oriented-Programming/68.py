## Creating special methods
# ที่ควรรู้จัก
# - `__repr__()` method = แสดง object ในรูปแบบให้คนเขียนโค้ด copy เอาไปสร้างใหม่ได้ง่ายๆ
# - `__str__()` method = สิ่งที่อยากให้ python แสดงผลเมื่อเอา `str()` มาครอบ object ของเรา

# สร้าง __repr__ method สำหรับ Item class
# ให้แสดงผลลัพธ์เป็น "Item('ชื่อสินค้า', ราคา, จำนวนสินค้าในคลัง)"
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

# สร้าง item_1 ใหม่ แล้วทดลองใช้ repr
item_1 = Item('PS5',20000,5)
print(repr(item_1))

# ลอง print item_1 ตรงๆ ดูเลย
print(item_1)

# ลองใช้ฟังก์ชัน str ครอบ item_1 แล้ว print ดู
print(str(item_1))

# เพิ่ม __str__ method สำหรับ Item class
# ที่แสดงผลลัพธ์เป็น "Product ID: รหัสผลิตภัฑณ์, Name: ชื่อสินค้า, Price: ราคา, Quantity: จำนวนสินค้นในคลัง"
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

# สร้าง item_1 ใหม่
# แล้วทดลองใช้ repr, str และ print item_1 ตรงๆ เปรียบเทียบกันดู
item_1 = Item('PS5',20000,5)
print(repr(item_1))
print(str(item_1))
print(item_1)

# สร้าง __add__ method สำหรับ Item class
# ที่อนุญาตให้เราเอา objects 2 อันที่เป็น Item class มาบวกกันได้
# โดยให้ผลลัพธ์เป็นผลรวมของ "มูลค่าสินค้าในคลัง" ซึ่งคือ ราคา * จำนวนสินค้าในคลัง
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

# ลองสร้าง item_1 และ item_2 ใหม่
# แล้วลองจับมันมาบวกกัน แล้วดูผลลัพธ์
item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)
print(item_1 + item_2)