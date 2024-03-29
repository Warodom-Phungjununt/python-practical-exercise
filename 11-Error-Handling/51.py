# กำหนด list ของ tip ที่ได้ในหน่วยดอลล่าร์ในรอบสัปดาห์ที่ผ่านมาซึ่งมีบางค่าหายไป
tip_usd = [2.50, 20, 80, None, -10.5, 25, None]
USD_TO_THB = 32.50

# ลองสร้าง tip_thb โดยสมมติว่าไม่มีข้อมูลที่ขาดหายไป
# แล้วดูว่าเกิด error อะไรขึ้น
tip_thb = []
for tip in tip_usd:
    try:
        tip_thb.append(tip*USD_TO_THB)
    except  TypeError:
        tip_thb.append(None)
print(tip_thb)

# พบว่ามีค่าแปลกๆ ที่ tip ติดลบ ซึ่งเรารับมือกรณีนี้ด้วยการ
# ให้ print ฟ้องว่ามีค่าแปลกๆ นี้ที่ index ตำแหน่งใดใน list ของเรา
# พร้อมระบุตัวเลขที่ติดลบนั้น
# และสุดท้าย เมื่อจบแต่ระรอบของ loop ให้ print ข้อความว่า
# 'Done with day i' โดย i คือลำดับใน list (เริ่มจาก 0 ได้)
# สร้าง tip_thb ขึ้นมาใหม่แทนของเดิมได้เลย

tip_thb = []
for i, tip in enumerate(tip_usd):
    try:
        tip_thb.append(tip*USD_TO_THB)
    except  TypeError:
        tip_thb.append(None)
    else:
        if tip < 0:
            print(f"Negative tip at index {i} with value {tip}")
    finally:
        print(f"Done with day {i+1}")