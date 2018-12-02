# -*- coding: utf-8 -*-
import scrapy
from lscarpy.items import LscarpyItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        item = LscarpyItem()
        articles = response.css('.archive-title')
        for article in articles:
            item['title'] = article.css('::text').extract_first()
            item['url'] = article.css('::attr("href")').extract_first()
            yield item

        next_page = response.css('a.next.page-numbers::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
