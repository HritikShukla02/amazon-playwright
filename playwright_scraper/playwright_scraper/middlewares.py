# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse

from playwright.sync_api import sync_playwright, expect


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class PlaywrightScraperSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class PlaywrightScraperDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


# class AmazonMiddleware:
#     def process_request(self, request, spider):
#         with sync_playwright() as p:
#             browser = p.chromium.launch()
#             page = browser.new_page()
#             page.goto(request.url)
#             # page.screenshot(path='amazon.png')
#             page.get_by_placeholder("Search Amazon.in", exact=True).fill("Kingston Pendrive 256GB")
#             page.get_by_placeholder("Search Amazon.in", exact=True).press("Enter")
#             expect(page.get_by_text("Check each product page for other buying options.")).to_be_visible()
#             # page.screenshot(path='amazon2.png', full_page=True)
#             # count = 2
#             # print(page.locator('css=span.s-pagination-disabled[aria-disabled="true"]'))
#             while not page.locator('span.s-pagination-disabled[aria-disabled="true"]:has-text("Next")').is_visible():
#                 # count += 1
#                 body = page.content()
#                 page.locator('a:has-text("Next")').click()
#                 expect(page.get_by_text("Need help?")).to_be_visible()

#                 response = HtmlResponse(url=page.url, body=body, encoding='utf-8', request=request)
#                 yield response
#                 # expect(page.get_by_role('navigation')).to_be_visible()

#                 # page.screenshot(path=f'amazon{count}.png', full_page=True)
        
#             # page.g
            

#             browser.close()

