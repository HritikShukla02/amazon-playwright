# amazon-playwright

This Scrapy spider conquers dynamic websites! Enter a keyword, and it leverages Playwright to render JavaScript-heavy pages. It then scrapes data across the first 10 pages of search results, wielding Scrapy's parsing power. Unleash it for keyword research, price comparisons, or content analysis!

### cloning the repo:
 - open the folder through cmd where you want to clone this scraper.
 - run the command: **git clone https://github.com/HritikShukla02/amazon-playwright.git**.

Since www.amazon.in has a very advanced spider detecting system we need to use proxy to bypass the checks. before starting with spider create a free account on **https://www.scraperapi.com**. You will get 5000 API credits for a free account that will do it for us.
### Setting up the environment:
 - cd into base directory: **cd amazon-playwright**.
 - Set up and your virtual environment with command **source .venv/bin/activate**.
 - Run command **pip3 install -r requirements.txt**.
 - create a **.env** file and store your scraperapi account's api-key in format: **API_KEY=YOURAPIKEY**.
 - If you are running this scraper for the first time you need to install the browser for playwright with command: **playwright install chromium**.

### Run the spider:
 - cd into the playwright-scraper directory of project with command: **cd playwright-scraper/playwright-scraper/spiders**.
 - open the file amazon_spider.py and edit the KEYWORD variable for what you want to search.
 - run the command: **scrapy crawl amazon_spider**

### Results:
 - You will be able to see the results in a new file named **results.json** created at the base of project.
 - If you want to check sample of output, check the output.json file that was resulted for keyword **pendrive**.


