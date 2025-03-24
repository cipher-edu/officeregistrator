import requests

BASE_URL = "https://student.nspi.uz/rest/v1"

# 1️⃣ Talaba login qilib token olish
def get_student_token(login, password):
    url = f"{BASE_URL}/auth/login"
    data = {"login": login, "password": password}  # `login` ishlatildi
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        token = response.json().get("data", {}).get("token")
        return token
    else:
        return {"error": f"Xatolik: {response.status_code}, {response.text}"}

# 2️⃣ Talabaning shaxsiy va akademik ma'lumotlarini olish
def get_student_info(token):
    url = f"{BASE_URL}/account/me"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Xatolik: {response.status_code}, {response.text}"}

# ✅ SHU YERGA HAQIQIY LOGIN VA PAROLNI KIRITING
login = "353211100388"  # `username` emas, `login` ishlatilmoqda
password = "3474710ja"

token = get_student_token(login, password)

if isinstance(token, str):
    print("✅ TOKEN:", token)
    student_info = get_student_info(token)
    print("🎓 Talaba ma'lumotlari:", student_info)
else:
    print("❌ Xatolik:", token)
