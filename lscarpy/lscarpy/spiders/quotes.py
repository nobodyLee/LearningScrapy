# -*- coding: utf-8 -*-
import scrapy
from lscarpy.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        item = QuotesItem()
        for quote in quotes:
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next_page = response.css('.pager .next a::attr("href")').extract_first()
        next_url = response.urljoin(next_page)
        if next_url is not None:
            yield response.follow(next_page, self.parse)
