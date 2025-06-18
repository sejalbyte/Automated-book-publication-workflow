from playwright.sync_api import sync_playwright
import os

# URL to scrape
URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

# Output paths
SCREENSHOT_PATH = "screenshots/chapter1.png"
TEXT_PATH = "data/original_chapter1.txt"

def scrape_and_capture():
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle")
        
        # Save full page screenshot
        page.screenshot(path=SCREENSHOT_PATH, full_page=True)

        # Extract text from main content div
        content = page.inner_text('div#mw-content-text')
        with open(TEXT_PATH, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[+] Scraped content saved to {TEXT_PATH}")
        print(f"[+] Screenshot saved to {SCREENSHOT_PATH}")
        browser.close()

if __name__ == "__main__":
    scrape_and_capture()
