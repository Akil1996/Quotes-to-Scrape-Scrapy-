import scrapy
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'titletext': title}
        # all_div_quotes = response.css("div.quote")
        # title = all_div_quotes.css('span.text::text').extract()
        # author = all_div_quotes.css(".author::text").extract()
        # tag = all_div_quotes.css(".tag::text").extract()
        # yield {
        #     'title':title,
        #     'author': author,
        #     'tag':tag
        # }
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

        next_page = "https://quotes.toscrape.com/page/"+str(QuoteSpider.page_number)+"/"
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)