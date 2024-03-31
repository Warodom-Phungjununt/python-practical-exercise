# สร้างสำรับไพ่ 52 ใบ ตั้งแต่ A♠, A♥, A♦, A♣, 2♠, ..., K♣
# บันทึกใส่ list ชื่อ my_deck
# จากนั้นสับไพ่ในสำรับ 10 รอบ
# print ผลของการสับแต่ละรอบ โดย print เฉพาะ 10 ใบแรกในสำรับ
import random

my_deck = []
alphanum = ['A', '2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K']
symbols = ['♠', '♥', '♦', '♣']

for a in alphanum:
    for s in symbols:
        my_deck.append(a + s)

print(my_deck)
print(len(my_deck))