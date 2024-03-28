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

# จงสร้าง set ใหม่ที่มีสมาชิกเป็นตัวอักษรตัวแรกของชื่อของแต่ละคน
# แต่เอาเฉพาะชื่อที่มีความยาวเท่ากับ 4 ตัวอักษรพอดี
# บันทึกใส่ตัวแปร first_letters_4
first_letters_4 = {name[0] for name in names if len(name) == 4}
print(first_letters_4)