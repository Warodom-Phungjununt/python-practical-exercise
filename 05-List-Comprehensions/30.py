# กำหนด list ของชื่อคนต่อไปนี้
names = [
    "James", "John", "Robert", "Michael", "William",
    "David", "Richard", "Joseph", "Thomas", "Charles",
    "Christopher", "Daniel", "Matthew", "Anthony", "Donald",
    "Mark", "Paul", "Steven", "Andrew", "Kenneth",
    "George", "Ronald", "Timothy", "Jason", "Jeffrey",
    "Ryan", "Jacob", "Gary", "Nicholas", "Eric",
    "Jonathan", "Stephen", "Larry", "Justin", "Scott",
    "Brandon", "Frank", "Benjamin", "Gregory", "Raymond",
    "Patrick", "Jack", "Dennis", "Jerry", "Tyler",
    "Aaron", "Jose", "Henry", "Douglas", "Adam",
    "Peter", "Nathan", "Zachary", "Walter", "Kyle",
    "Harold", "Carl", "Jeremy", "Keith", "Roger",
    "Gerald", "Ethan", "Arthur", "Terry", "Christian",
    "Sean", "Lawrence", "Austin", "Joe", "Noah",
    "Jesse", "Albert", "Bryan", "Billy", "Bruce",
    "Willie", "Gabriel", "Gordon", "Samuel", "Geoffrey",
    "Glenn", "Gene", "Gilbert", "Gavin", "Gage"
]

# Ex4 : จงสร้าง list ใหม่ที่มีเฉพาะชื่อคนที่ขึ้นต้นด้วยตัว G เท่านั้น
# บันทึกใส่ตัวแปร names_G
names_G = [name for name in names if name[0] == 'G']
print(names_G)