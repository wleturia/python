# -*- coding: utf-8 -*-
import scrapy

from reddit.items import RedditItem
from scrapy.http.request import Request

class RedditJobSpider(scrapy.Spider):
    #Where to extract data
    name = 'reddit_job'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/r/funny/']

    def parse(self, response):
        #How to extract data      
        titles = print(response.css("a::text").extract())
        hrefs = print(response.css("a::text").extract())
        scores = print(response.css("a::text").extract())

        for item in zip(titles,hrefs,scores):
            new_item = RedditItem()

            new_item['title'] = item[0]
            new_item['href'] = item[1]
            new_item['score'] = item[2]

            yield new_item

        next_page = response.css("span.next-button").css('a::attr(href)').extract()[0]

        yield Request(url = next_page, callback= self.parse)