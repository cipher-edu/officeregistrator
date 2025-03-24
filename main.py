import requests

API_KEY = "vdOnRuIxrl6iSGImiC-ztAiS5hcpF5qhE7oRjSTT"

URL = "https://student.hemis.uz/rest/v1/students/me"  # HEMIS API hujjatlaridan tekshirib oling

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.get(URL, headers=headers)

print(response.status_code)
print(response.text)
