# กำหนด dict ดังนี้
months = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
    'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}

# จงสร้าง dict ที่สลับเอาเลขเดือนเป็น key แทน และ value เป็นชื่อย่อเดือน
# บันทึกใส่ตัวแปรเดิมได้เลย
months = {num: month for month, num in months.items()}
print(months)