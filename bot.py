import requests
import time

# تنظیمات اولیه
GRASS_API_URL = "https://api.getgrass.io/farm"  # آدرس API (فعلاً فرضی)
API_KEY = "your_api_key_here"  # کلید API (فعلاً فرضی)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# تابع برای بررسی موجودی
def check_balance():
    response = requests.get(f"{GRASS_API_URL}/balance", headers=headers)
    if response.status_code == 200:
        balance = response.json().get("balance")
        print(f"Your $GRASS balance: {balance}")
        return balance
    else:
        print("Error checking balance")
        return None

# تابع برای انجام فارمینگ
def perform_farming():
    response = requests.post(f"{GRASS_API_URL}/farm", headers=headers)
    if response.status_code == 200:
        print("Farming successful!")
    else:
        print("Error during farming")

# حلقه اصلی برای فارمینگ مداوم
def main():
    while True:
        check_balance()
        perform_farming()
        time.sleep(300)  # هر 5 دقیقه یکبار اجرا می‌شه

if __name__ == "__main__":
    main()
