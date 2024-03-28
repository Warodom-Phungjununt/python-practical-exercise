# สมมติมี list ของชื่อนักแสดงชายดังนี้
actors = ["Cillian Murphy", "Matt Damon", "Robert Downey Jr.", "Josh Hartnett"]

# วิธีเก่า
# actors_initial = dict()
# for name in actors:
#     key = name
#     value = name[0]
#     actors_initial[key] = value
# print(actors_initial)

# จงสร้าง dict ที่มี key เป็นชื่อเต็มและ value เป็นหนังสือตัวแรกของชื่อ
# บันทึกใส่ actors_initial
actors_initial = {x: x[0] for x in actors}
print(actors_initial)