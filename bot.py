import requests
import time

# تنظیمات اولیه
GRASS_API_URL = "https://api.getgrass.io"  # آدرس پایه API
API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJseGtPeW9QaWIwMlNzUlpGeHBaN2JlSzJOSEJBMSJ9.eyJlbWFpbCI6InJhYmlvcDc4MkBnbWFpbC5jb20iLCJzY29wZSI6IlVTRVIiLCJ1c2VySWQiOiIydmd4VE5hMlhNUmF5cU00NEI4QUw0cGVaR2siLCJpYXQiOjE3NDQ1ODA4MjEsIm5iZiI6MTc0NDU4MDgyMSwiZXhwIjoxNzQ0NjY3MjIxLCJhdWQiOiJ3eW5kLXVzZXJzIiwiaXNzIjoiaHR0cHM6Ly93eW5kLnMzLmFtYXpvbmF3cy5jb20vcHVibGljIn0.DG9fPDGZ_VKCcmmCENRmmKpLd4VHkelz-3yB5_wT2RCBkLvz6AKig4EKm2cFViozh9yHvXKtGe7MAVrnUvwH6SQtLvS-WL6GuFrq124MDRNY8AsR06kLpoekuo5jESDXldt0ZaekZKnpDrmZA-I_54kn46yzogtt2a8-1TnyhrA2_Bb9zAAFbTBDdkh6whQRp-NQNsZq3NSIxMArIjFLp978Bq0m8imPzZsB50p8aOD-OpzJSxSwm3BbGcInkfSiwytsK6kA0q_6iZOKpttp1kMNVyCwyhiAGuehUXRVkqtXcpNdm1ZAjQr-WmvtNjbTNvZoo8ZsZ1sSo-LmEHDSkw"  # توکن Authorization

headers = {
    "Authorization": f"Bearer {API_KEY}",  # توکن برای احراز هویت
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537 7.0.0.0 Safari/5.0",  # User-Agent
    "Accept": "application/json",  # نوع داده‌ای که قبول می‌کنیم
    "Referer": "https://app.getground.io/",  # برای تقلید مرورگر
    "Origin": "https://app.getground.io"  # برای تlng browser simulation
}

# تابع برای بررسی درآمد روزانه
def check_daily_earnings():
    params = {"input": '{"limit":25}'}  # پارامترهای درخواست
    response = requests.get(f"{GRASS_API_URL}/dailyEarnings", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        total_earnings = sum(item.get("earnings", 0) for item in data)  # جمع درآمدهای روزانه
        print(f"جمع درآمد روزانه $GRASS شما (25 روز اخیر): {total_earnings}")
        return total_earnings
    else:
        print(f"خطا در بررسی درآمد روزانه: {response.status_code} - {response.text}")
        return None

# تابع برای بررسی درآمد دوره‌ای (epoch)
def check_epoch_earnings():
    params = {"input": '{"limit":1,"isLatestOnly":true}'}  # پارامترهای درخواست
    response = requests.get(f"{GRASS_API_URL}/epochEarnings", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        epoch_earnings = data[0].get("earnings", 0) if data else 0
        print(f"درآمد دوره‌ای $GRASS شما (آخرین دوره): {epoch_earnings}")
        return epoch_earnings
    else:
        print(f"خطا در بررسی درآمد دوره‌ای: {response.status_code} - {response.text}")
        return None

# تابع برای بررسی درآمد بر اساس IP
def check_ip_earnings():
    response = requests.get(f"{GRASS_API_URL}/ipEarnings", headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_ip_earnings = sum(item.get("earnings", 0) for item in data) if isinstance(data, list) else data.get("earnings", 0)
        print(f"جمع درآمد $GRASS شما از IP‌ها: {total_ip_earnings}")
        return total_ip_earnings
    else:
        print(f"خطا در بررسی درآمد IP: {response.status_code} - {response.text}")
        return None

# تابع برای بررسی دستگاه‌ها
def check_devices():
    params = {"input": '{"limit":5}'}  # پارامترهای درخواست
    response = requests.get(f"{GRASS_API_URL}/devices", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"دستگاه‌های متصل به حساب شما: {data}")
        return data
    else:
        print(f"خطا در بررسی دستگاه‌ها: {response.status_code} - {response.text}")
        return None

# تابع برای تقلید فارمینگ
def perform_farming():
    # تقلید درخواست افزونه با ارسال یه درخواست به یه مسیر احتمالی
    # این مسیر ممکنه درست نباشه، باید API فارمینگ رو پیدا کنیم
    response = requests.post(f"{GRASS_API_URL}/connect", headers=headers)
    if response.status_code == 200:
        print("فارمینگ (تقلید) با موفقیت انجام شد!")
    else:
        print(f"خطا در فارمینگ (تقلید): {response.status_code} - {response.text}")

# حلقه اصلی برای بررسی و فارمینگ
def main():
    while True:
        check_daily_earnings()
        check_epoch_earnings()
        check_ip_earnings()
        check_devices()
        perform_farming()
        print("در انتظار 5 دقیقه برای بررسی بعدی...")
        time.sleep(300)  # هر 5 دقیقه یکبار اجرا می‌شه

if __name__ == "__main__":
    main()
