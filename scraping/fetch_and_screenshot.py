from playwright.sync_api import sync_playwright
import os

def fetch_and_screenshot(url, save_path):
    os.makedirs(save_path, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        page.screenshot(path=f"{save_path}/screenshot.png")
        with open(f"{save_path}/content.txt", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
    return content
