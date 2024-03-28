# กำหนดค่าตัวแปร
product_name = "Laptop"
price = float(1200.5)
quantity = int(3)

# คำนวณ total_cost
total_cost = price * quantity

# สร้างข้อมูลด้วย Format Method
Product_Information = "Product: {}\
Price: ${:.2f}\
Quantity: {}\
Total Cost: ${:.2f}".format(product_name, price, quantity, total_cost)

# แสดงค่าออกมา
print(Product_Information)

# -----------[Output]-----------

# Product: Laptop
# Price: $1200.50
# Quantity: 3
# Total Cost: $3601.50