import scrapy
from scrapy.utils.response import open_in_browser
from ..items import QuotesItem
from scrapy.http import FormRequest
class QuoteSpider(scrapy.Spider):
    name = "quote"
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response,):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            "csrf_token" : token,
            "username": 'akilh4@gmail.com',
            "password": "Akil@2007"
        },callback = self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotesItem()
        all_div_quotes = response.css("div.quote")
        for q in all_div_quotes:
            title = q.css('span.text::text').extract()
            author = q.css(".author::text").extract()
            tag = q.css(".tag::text").extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = "https://quotes.toscrape.com/page/" + str(QuoteSpider.page_number) + "/"
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.start_scraping)