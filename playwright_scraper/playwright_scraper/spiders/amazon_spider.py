import scrapy
from scrapy_playwright.page import PageMethod
from playwright_scraper.items import PlaywrightScraperItem
from urllib.parse import urlencode
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


API_KEY = os.getenv('API_KEY')
KEYWORD = 'pendrive'


def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    # allowed_domains = ["www.amazon.in", "proxy.scrapeops.io"]
    start_urls = [f"https://www.amazon.in/s?k={KEYWORD}",]


    def start_requests(self):
        for i in range(10):
            url = self.start_urls[0] + "&page=" + str(i)
            yield scrapy.Request(get_proxy_url(url), meta=dict(
                playwright =  True,
                playwright_page_methods = [
                   PageMethod("wait_for_selector", 'div.s-pagination-container[role="navigation"]'),  # Replace with a selector that indicates the form was submitted
                ],
                errback=self.errback
            ))


    async def parse(self, response):
        
        links = response.css('div.a-section.s-title-instructions-style[data-cy="title-recipe"] h2 a::attr(href)').getall()
        # links_ = ['https://www.amazon.in' + link for link in links]
        for link in links:
            url = 'https://www.amazon.in' + link
                    
            yield scrapy.Request(get_proxy_url(url), callback=self.parse_item, 
                meta=dict(
                playwright = True,
                playwright_include_page = True,
                playwright_page_methods = [
                    PageMethod('wait_for_selector', 'table.a-normal.a-spacing-micro'),
                ]),
                errback=self.errback
            )


    async def parse_item(self, response):
        page = response.meta["playwright_page"]
        # await page.wait_for_timeout(20 * 1000)
        await page.close()
        item = PlaywrightScraperItem()

        table = response.css('table.a-normal.a-spacing-micro tr')

        item['name'] = response.css('h1#title span#productTitle ::text').get().strip()
        item['price'] = response.css('span.a-price-whole ::text').get()
        item['brand'] = response.css('table tr td.a-span9 span ::text').get()
        item['memory'] = table[1].css('td.a-span9 span ::text').get()
        item['h_w_interface'] = table[2].css('td.a-span9 span ::text').get()
        item['special_features'] = table[3].css('td.a-span9 span ::text').get()
        item['read_speed'] = table[4].css('td.a-span9 span ::text').get()


        yield item


    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
        



