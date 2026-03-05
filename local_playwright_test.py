import os
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 800})
    
    # 1. Anketler Sayfası
    page.goto("http://127.0.0.1:8000/polls/")
    page.screenshot(path="screenshot_1_index.png", full_page=True)
    print("✅ Anketler (index) sayfasının ekran görüntüsü alındı.")
    
    # 2. Giriş Yap (Kullanıcı Değiştir) Sayfası
    page.goto("http://127.0.0.1:8000/polls/switch/")
    page.fill("#id_password", "TestPassword123!")
    
    toggle_btns = page.locator("button.absolute")
    if toggle_btns.count() > 0:
        toggle_btns.first.click()
        print("✅ Şifre Göz ikonuna tıklandı (Giriş).")
    
    page.screenshot(path="screenshot_2_login.png")
    print("✅ Giriş yap sayfasının ekran görüntüsü alındı.")

    # 3. Kayıt Ol Sayfası
    page.goto("http://127.0.0.1:8000/polls/register/")
    page.fill("input[name='password1']", "NewPassword123!")
    
    toggle_btns2 = page.locator("button.absolute")
    if toggle_btns2.count() > 0:
        toggle_btns2.first.click()
        print("✅ Şifre Göz ikonuna tıklandı (Kayıt).")

    page.screenshot(path="screenshot_3_register.png")
    print("✅ Kayıt ol sayfasının ekran görüntüsü alındı.")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
