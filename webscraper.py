from playwright.async_api import  async_playwright
import asyncio




async def run(monthnm, regno):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://www.gkvedu.in/result2017.aspx")
        await page.get_by_role("button", name=monthnm).click()
        await page.locator("#ctl00_ContentPlaceHolder1_TxtRoll_No").click()
        await page.locator("#ctl00_ContentPlaceHolder1_TxtRoll_No").fill(regno)
        await page.get_by_role("button", name="Print").click()
        await page.wait_for_timeout(1500)
        for i in range(0,11):
            await page.keyboard.down('Tab')
            await page.keyboard.up('Tab')
        await page.keyboard.down('Space')
        await page.keyboard.up('Tab')
        # await page.get_by_role("table",name='Export').get_by_role('cell',name= 'Export').click()
        async with page.expect_download() as download_info:
            await page.get_by_role("link", name="PDF").click()
        download = await download_info.value
        await download.save_as("./Result/Report.pdf")
        await browser.close()

async def resultmonthscraper():
    async with async_playwright() as p:
        months = []
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://www.gkvedu.in/result2017.aspx")
        table  = page.locator('//*[@id="aspnetForm"]/div[3]/table/tbody/tr[2]/td[2]')
        count = await table.count()
        print(table)
        for i in range(count):
            elem = table.nth(i)
            attrvalue = await elem.get_attribute('value')
            print(attrvalue)
            

#asyncio.run(resultmonthscraper())