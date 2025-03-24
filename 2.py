import requests

BASE_URL = "https://student.nspi.uz/rest/v1"
TOKEN = "N2WC2dH2rTkbSZjzHCErMPJibgpQEXRVGky7o9xf"  # ✅ Admin paneldan olingan tokenni shu yerga qo'ying

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# 1️⃣ Talabalar ro‘yxatini olish
def get_students(page=1, limit=10):
    url = f"{BASE_URL}/data/student-list?page={page}&limit={limit}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Xatolik: {response.status_code}, {response.text}"}

# 2️⃣ Dars jadvalini olish
def get_schedule(page=1, limit=10):
    url = f"{BASE_URL}/data/schedule-list?page={page}&limit={limit}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Xatolik: {response.status_code}, {response.text}"}

# 3️⃣ Imtihon natijalarini olish
def get_exam_results(page=1, limit=10):
    url = f"{BASE_URL}/data/student-performance-list?page={page}&limit={limit}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Xatolik: {response.status_code}, {response.text}"}

# ✅ Ma'lumotlarni chaqirish
students = get_students()
schedule = get_schedule()
exam_results = get_exam_results()

print("📌 Talabalar:", students)
print("📌 Dars jadvali:", schedule)
print("📌 Imtihon natijalari:", exam_results)
print("API TOKEN:", TOKEN)

