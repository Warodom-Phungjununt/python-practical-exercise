# (Challenge) สร้างเกมส์เป่ายิ้งฉุบระหว่าง 2 ผู้เล่น
# ให้สุ่มเล่นไปเรื่อยๆ จนกว่าจะมีผู้ชนะ
# โดยผู้ชนะคือ ชนะ 3 ตาได้ก่อน
# ให้ print ผลของแต่ละตา
# และ print ผู้ชนะในตอนสุดท้าย

import random

p1_points = 0
p2_points = 0
weapons = ['rock','scissor','paper']

def play(p1, p2):
    if p1 == p2:
        return 'draw'
    if p1 == 'rock':
        if p2 == 'scissor':
            return 'P1'
        else:
            return 'P2'
    if p1 == 'paper':
        if p2 == 'rock':
            return 'P1'
        else:
            return 'P2'
        
while (p1_points<3) and (p2_points<3):
    p1_weapon = random.choice(weapons)
    p2_weapon = random.choice(weapons)

    result = play(p1_weapon, p2_weapon)

    if result == 'P1':
        p1_points = p1_points + 1
        print(f'P1 is {p1_weapon} and P2 is {p2_weapon} --> P1 wins !')
    elif result == 'P2':
        p2_points = p2_points + 1
        print(f'P1 is {p1_weapon} and P2 is {p2_weapon} --> P2 wins !')
    else:
        print(f'P1 is {p1_weapon} and P2 is {p2_weapon} --> Draw !')
    
    print(f'Current, score for P1 is {p1_points} and P2 is {p2_points}')

if p1_points == 3:
    print(f'The winner is P1!!!')
else:
    print(f'The winner is P2!!!')