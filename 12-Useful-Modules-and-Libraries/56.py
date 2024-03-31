import random
# เล่นสุ่มกาชาปอง โดยมีของใน list ต่อไปนี้
gashapon_items = ['หมวกแมว','ชินจัง','นารูโตะ','ลูฟี่','อาเนีย','กล่องเปล่า','กล่องเปล่า','กล่องเปล่า']
# วนลูป 3 รอบเพื่อสุ่มของจาก gashapon_items
# โดยของที่ถูกหยิบออกไปแล้ว จะต้องเอาออกจาก list
# เอาของที่ถูกหยิบออกมาใส่ใน list ใหม่ชื่อ collected_items
collected_items = []

for i in range(3):
    item = random.choice(gashapon_items)
    gashapon_items.remove(item)
    collected_items.append(item)
print(gashapon_items)
print(collected_items)