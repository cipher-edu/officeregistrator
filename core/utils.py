import requests
from .models import Student  

BASE_URL = "https://student.nspi.uz/rest/v1"

# 1️⃣ Student API orqali login va token olish
def get_student_token(login, password):
    url = f"{BASE_URL}/auth/login"
    data = {"login": login, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)
    print("🔍 Token olish javobi:", response.status_code, response.text)  # ✅ Token natijasini tekshirish

    if response.status_code == 200:
        return response.json().get("data", {}).get("token")
    else:
        return None

# 2️⃣ Talabaning shaxsiy ma'lumotlarini olish
def get_student_info(token):
    url = f"{BASE_URL}/account/me"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("📌 Student info javobi:", response.status_code, response.text)  # ✅ Ma'lumotlarni tekshirish

    if response.status_code == 200:
        return response.json().get("data", {})
    else:
        return None

# 3️⃣ Talabaning ma'lumotlarini saqlash
# def save_student_to_db(login, password):
#     print(f"✅ Login: {login}, Parol: {password}")
#     token = get_student_token(login, password)

#     if token:
#         print("✅ Token olindi:", token)
#         student_data = get_student_info(token)

#         if student_data:
#             print("✅ Talaba ma'lumotlari:", student_data)

#             student, created = Student.objects.update_or_create(
#                 student_id=student_data.get("student_id_number"),  # ✅ To‘g‘ri ID olish
#                 defaults={
#                     "full_name": student_data.get("full_name"),
#                     "email": student_data.get("email"),
#                     "phone": student_data.get("phone"),
#                     "faculty": student_data.get("faculty", {}).get("name"),
#                     "group": student_data.get("group", {}).get("name"),
#                     "token": token,
#                 }
#             )
#             print("✅ Ma'lumot bazaga saqlandi!")
#             return student
#         else:
#             print("❌ Talaba ma'lumotlari API'dan kelmadi!")
#     else:
#         print("❌ Token olinmadi!")

#     return None
def save_student_to_db(login, password):
    token = get_student_token(login, password)

    if token:
        student_data = get_student_info(token)

        if student_data:
            student, created = Student.objects.update_or_create(
                student_id=student_data.get("student_id_number"),  # ✅ To‘g‘ri kalit ishlatilmoqda
                defaults={
                    "full_name": student_data.get("full_name"),
                    "email": student_data.get("email"),
                    "phone": student_data.get("phone"),
                    "faculty": student_data.get("faculty", {}).get("name"),  # ✅
                    "group": student_data.get("group", {}).get("name"),  # ✅
                    "university": student_data.get("university"),  # ✅
                    "specialty": student_data.get("specialty", {}).get("name"),  # ✅
                    "birth_date": student_data.get("birth_date"),  # ✅
                    "passport_pin": student_data.get("passport_pin"),  # ✅
                    "passport_number": student_data.get("passport_number"),  # ✅
                    "gender": student_data.get("gender", {}).get("name"),  # ✅
                    "education_form": student_data.get("educationForm", {}).get("name"),  # ✅
                    "education_type": student_data.get("educationType", {}).get("name"),  # ✅
                    "payment_form": student_data.get("paymentForm", {}).get("name"),  # ✅
                    "address": student_data.get("address"),  # ✅
                    "accommodation": student_data.get("accommodation", {}).get("name"),  # ✅
                    "level": student_data.get("level", {}).get("name"),  # ✅
                    "semester": student_data.get("semester", {}).get("name"),  # ✅
                    "image": student_data.get("image"),  # ✅
                }
            )
            print("✅ Ma'lumot bazaga saqlandi!")
            return student
        else:
            print("❌ Talaba ma'lumotlari API'dan kelmadi!")
    else:
        print("❌ Token olinmadi!")

    return None
