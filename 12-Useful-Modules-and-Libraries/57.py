import random
# สถานการณ์เดียวกับเมื่อกี๊ แต่ใช้วิธีหยิบของทีเดียว 3 อย่างเลย ไม่ต้องวนลูป
# ระวังว่าห้ามหยิบของซ้ำ เช่น หมวกแมวมีอันเดียว ผลลัพธ์ห้ามมีหมวกแมวมากกว่า 1 อัน
gashapon_items = ['หมวกแมว','ชินจัง','นารูโตะ','ลูฟี่','อาเนีย','กล่องเปล่า','กล่องเปล่า','กล่องเปล่า']
collected_items = random.sample(gashapon_items, 3)

print(gashapon_items)
print(collected_items)