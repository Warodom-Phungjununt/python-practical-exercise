# Scenario: ในโลกจริง เราจำเป็นต้องมีคลังข้อมูล (Database) ในการเก็บข้อมูล ซึ่งมีเทคโนโลยี Database ให้ใช้มากมายแล้วแต่ความต้องการ เช่น MySQL, MongoDB เป็นต้น แต่เนื่องจากคอร์สนี้เราจะยังไม่ไปแตะเทคโนโลยีเหล่านั้น เราเลยจะ "จำลอง" Database ขึ้นมา ด้วยการสร้าง class ชื่อ StoreDB ซึ่งมี methods ดังนี้

# 1. `__init__` method: มี attribute ชื่อ `items` ซึ่งเริ่มต้นเป็น dict เปล่าๆ
# 2. `add_item` method: รับ parameter เป็น Item object แล้วเพิ่ม object นี้เข้า `items` dict โดย key = product_id และ value = item ที่รับเข้ามา
# 3. `remove_item` method: รับ parameter เป็น product_id ซึ่งถ้าใน `items` dict มี product_id นี้อยู่ ให้เอา object นั้นออกจาก dict
# 4. `print_items` method: print บอกว่าตอนนี้มีผลิตภัณฑ์ใน `items` dict อยู่กี่ผลิตภัณฑ์ ซึ่งถ้าไม่เป็นศูนย์ ให้ print บอกด้วยว่ามีผลิตภัณฑ์อะไรอยู่บ้าง โดยอาจใช้ `__str__` method ของ Item class ในการ print แสดงผลได้

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

class Book(Item):

    def __init__(self, name, price, stock_quantity, author, num_pages):
        super().__init__(name, price, stock_quantity)
        self.author = author
        self.num_pages = num_pages
    
    def __repr__(self):
        return f"Book('{self.name}',{self.price},{self.stock_quantity},'{self.author}',{self.num_pages})"
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.stock_quantity} Author: {self.author} Pages Number: {self.num_pages}"
    
class StoreDB():

    def __init__(self):
        self.items = dict()
    
    def add_items(self, items):
        self.items[items.product_id] = items
        print("Successfully added item {}".format(repr(items)))

    def remove_item(self, product_id):
        if product_id in self.items.keys():
            removed_item = self.items.pop(product_id)
            print("Successfully removed item {}".format(repr(removed_item)))
        else:
            print("No product with product id {}".format(product_id))
    
    def print_items(self):
        if len(self.items) == 0:
            print("No items in the store!")
        else:
            print("There are {} items in our store.".format(len(self.items)))
            for item in self.items.values():
                print("--" + str(item))

store = StoreDB()
store.print_items()

item_1 = Item('PS5', 20000, 5)
item_2 = Item('Nintentendo Switch', 15000, 10)
book_1 = Book("ถ้าโลกนี้มีแต่แมวส้ม", 555, 10000, "พรี่เกรท", 123)
book_2 = Book("น่าจะรู้งี้ตั้งแต่อายุ 5 ขวบ", 20, 5, "พรี่เกรท", 2)
print(item_1)
print(item_2)
print(book_1)
print(book_2)

store.add_items(item_1)
store.add_items(item_2)
store.add_items(book_1)
store.add_items(book_2)

store.print_items()

store.remove_item("P-000004")
store.print_items()

store.remove_item("P-999999")