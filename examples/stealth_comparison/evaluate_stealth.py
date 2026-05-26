import os
import sys
import asyncio

# Target URLs for bot detection / fingerprinting tests
TARGETS = {
    "sannysoft": "https://bot.sannysoft.com/",
    "fingerprintjs": "https://fingerprint.com/products/bot-detection/",
    "httpbin_headers": "https://httpbin.org/headers"
}

OUTPUT_DIR = "./output/stealth_comparison"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_standard_playwright():
    """Runs a standard Playwright automation and captures results."""
    print("\n=== Menjalankan Playwright Standar ===")
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("[Error] Playwright tidak terinstal. Jalankan: pip install playwright")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Test 1: Sannysoft Bot Detection
        print(f"Mengakses {TARGETS['sannysoft']}...")
        await page.goto(TARGETS['sannysoft'])
        await page.wait_for_timeout(3000)
        screenshot_path = os.path.join(OUTPUT_DIR, "playwright_standard_sannysoft.png")
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot disimpan ke: {screenshot_path}")

        # Test 2: FingerprintJS Bot Detection Demo
        print(f"Mengakses {TARGETS['fingerprintjs']}...")
        await page.goto(TARGETS['fingerprintjs'])
        await page.wait_for_timeout(3000)
        screenshot_path = os.path.join(OUTPUT_DIR, "playwright_standard_fingerprintjs.png")
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot disimpan ke: {screenshot_path}")

        await browser.close()

async def run_cloak_browser():
    """Runs CloakBrowser automation with stealth patches and humanized inputs."""
    print("\n=== Menjalankan CloakBrowser ===")
    try:
        from cloakbrowser import launch_context_async
    except ImportError:
        print("[Info] cloakbrowser tidak terinstal di lingkungan ini.")
        print("Untuk menguji CloakBrowser, silakan instal menggunakan: pip install cloakbrowser")
        return

    # launch_context_async handles CloakBrowser launch under the hood
    print("Memulai CloakBrowser dengan stealth patches & humanize=True...")
    context = await launch_context_async(
        headless=True,
        humanize=True,
        human_preset="careful"
    )
    page = await context.new_page()

    # Test 1: Sannysoft Bot Detection
    print(f"Mengakses {TARGETS['sannysoft']}...")
    await page.goto(TARGETS['sannysoft'])
    await page.wait_for_timeout(3000)
    screenshot_path = os.path.join(OUTPUT_DIR, "cloakbrowser_sannysoft.png")
    await page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot disimpan ke: {screenshot_path}")

    # Test 2: FingerprintJS Bot Detection Demo
    print(f"Mengakses {TARGETS['fingerprintjs']}...")
    await page.goto(TARGETS['fingerprintjs'])
    await page.wait_for_timeout(3000)
    screenshot_path = os.path.join(OUTPUT_DIR, "cloakbrowser_fingerprintjs.png")
    await page.screenshot(path=screenshot_path)
    print(f"Screenshot disimpan ke: {screenshot_path}")

    await context.close()

async def main():
    # Run standard Playwright test
    await run_standard_playwright()
    
    # Run CloakBrowser test
    await run_cloak_browser()

if __name__ == "__main__":
    asyncio.run(main())
