# import asyncio
from playwright.sync_api import expect, sync_playwright
# async def main():
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.amazon.in/")
    page.screenshot(path='amazon.png')
    page.get_by_placeholder("Search Amazon.in", exact=True).fill("Kingston Pendrive 256GB")
    page.get_by_placeholder("Search Amazon.in", exact=True).press("Enter")
    expect(page.get_by_text("Check each product page for other buying options.")).to_be_visible()
    page.screenshot(path='amazon2.png', full_page=True)
    count = 2
    # print(page.locator('css=span.s-pagination-disabled[aria-disabled="true"]'))
    while not page.locator('span.s-pagination-disabled[aria-disabled="true"]:has-text("Next")').is_visible():
        count += 1
        page.locator('a:has-text("Next")').click()
        expect(page.get_by_text("Need help?")).to_be_visible()
        # expect(page.get_by_role('navigation')).to_be_visible()

        page.screenshot(path=f'amazon{count}.png', full_page=True)
   
    # page.g
    

    browser.close()


    