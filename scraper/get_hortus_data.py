import asyncio
from playwright.async_api import async_playwright, expect
import html2text
import json
from datetime import datetime
import os


async def gather_elements_data(elements):
    json_objects = []
    for element in elements:
        json_objects.append(
            {
                "text": html2text.html2text(
                    await element.get_attribute("data-title") or ""
                ),
                "image_url": await element.get_attribute("href") or "",
                "link_instagram": await element.get_attribute("data-url") or "",
                "scraping_date": datetime.now().isoformat(),
            }
        )
    return json_objects


async def save_data_to_json(data, folder="data_flowers", filename="flowers_tiles"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(
        folder, f"{filename}_{datetime.now().strftime('%d_%m_%Y')}.json"
    )
    with open(filepath, "w") as f:
        json.dump(data, f)


async def save_html_content(page, filepath):
    await expect(page.get_by_text("Website ontwikkeling")).to_be_visible()
    with open(filepath, "w") as f:
        f.write(await page.content())


async def scrape_blog_buttons(page, button_locator, folder="blog_html_files"):
    os.makedirs(folder, exist_ok=True)
    buttons = await button_locator.all()
    for i, blog in enumerate(buttons):
        await blog.click()
        await save_html_content(page, filepath=f"{folder}/blog_{i}.html")
        await page.go_back(wait_until="load")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        url = "https://www.dehortus.nl/en/"
        await page.goto(url)

        await page.wait_for_selector("text=Website ontwikkeling")

        # Gathering and saving elements data
        elements_locator = page.locator(
            "//div[@class='sbi_inner_wrap']//a[@class='sbi_link_area nofancybox']"
        )
        data_to_json = {
            "flowers": await gather_elements_data(await elements_locator.all())
        }
        await save_data_to_json(data_to_json)

        # Scraping and screenshotting blog buttons
        blogs_button_locator = page.locator(
            "//div[@class='headerslider']//div[contains(@class,'slide cycle-slide')]//div[@class='col-lg-5 col-md-7']//a[(@class='button') and (not(@style))]"
        )
        await scrape_blog_buttons(page, blogs_button_locator)

        await browser.close()


asyncio.run(main())
