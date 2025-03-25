import requests
import json
from datetime import datetime
from getpass import getpass

class HemisAPI:
    def __init__(self):
        self.base_url = "https://student.nspi.uz/rest/"  # URL ni tekshirib oling
        self.session = requests.Session()
        self.token = None
        self.refresh_token = None

    def login(self, username, password):
        """Tizimga kirish"""
        url = f"{self.base_url}v1/auth/login"
        payload = {
            "login": username,
            "password": password
        }
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                self.token = data['data']['token']
                self.refresh_token = response.cookies.get('refresh-token')
                return True
            else:
                print(f"Xato: {data.get('error', 'Noma\'lum xato')}")  # Corrected without backslash issues
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"Tarmoq xatosi: {str(e)}")
            return False

    def get_account_info(self):
        """Talaba ma'lumotlarini olish"""
        if not self.token:
            print("Avval tizimga kiring!")
            return None
            
        url = f"{self.base_url}v1/account/me"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        
        try:
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ma'lumotlarni olishda xato: {str(e)}")
            return None

    def get_schedule(self, week=None, semester=None):
        """Dars jadvalini olish"""
        if not self.token:
            print("Avval tizimga kiring!")
            return None
            
        url = f"{self.base_url}v1/education/schedule"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {}
        
        if week: params['week'] = week
        if semester: params['semester'] = semester
        
        try:
            response = self.session.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Jadvalni olishda xato: {str(e)}")
            return None

    def get_grades(self):
        """Baholarni olish"""
        if not self.token:
            print("Avval tizimga kiring!")
            return None
            
        url = f"{self.base_url}v1/education/performance"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        
        try:
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Baholarni olishda xato: {str(e)}")
            return None

if __name__ == "__main__":
    print("HEMIS API Dasturi")
    print("=" * 30)
    
    api = HemisAPI()
    
    # Kirish
    username = input("ID raqam: ").strip()
    password = getpass("Parol: ").strip()
    
    if api.login(username, password):
        print("\nMuvaffaqiyatli kirish!")
        
        # Talaba ma'lumotlari
        print("\nTalaba ma'lumotlari:")
        account_info = api.get_account_info()
        if account_info:
            print(json.dumps(account_info, indent=2, ensure_ascii=False))
        
        # Dars jadvali
        print("\nDars jadvali:")
        schedule = api.get_schedule()
        if schedule:
            print(json.dumps(schedule, indent=2, ensure_ascii=False))
        
        # Baholar
        print("\nBaholar:")
        grades = api.get_grades()
        if grades:
            print(json.dumps(grades, indent=2, ensure_ascii=False))
    else:
        print("\nKirish amalga oshmadi. Iltimos, login va parolni tekshiring.")