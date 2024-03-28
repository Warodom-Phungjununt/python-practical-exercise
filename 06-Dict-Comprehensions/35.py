# (Challenge) ให้ value เป็นตัวหนังสือตัวแรกของชื่อและนามสกุลมาต่อกัน เช่น
# Cillian Murphy = CM
# Robert Downey Jr. = RDJ
# บันทึกใส่ actors_initials

def extract_initials(full_name):
    name_parts = full_name.split()
    initials = [part[0] for part in name_parts]
    final_result = ''.join(initials)
    return final_result

actors = ["Cillian Murphy", "Matt Damon", "Robert Downey Jr.", "Josh Hartnett"]
actors_initials = {name: extract_initials(name) for name in actors}
print(actors_initials)