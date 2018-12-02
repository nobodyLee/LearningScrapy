# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LscarpyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()


class QuotesItem(scrapy.Item):
    """Define the fields for quotes item here"""
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
