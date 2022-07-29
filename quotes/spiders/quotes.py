import scrapy
from ..items import QuotesItem

class quots(scrapy.Spider):
        name="sp1"
        start_urls=["https://quotes.toscrape.com/"]
        def parse(self, response):
            items=QuotesItem()
            for item in response.css("div.quote"):
                items['text'] = item.css("span.text::text").get()
                items["author"]=item.css("small.author::text").get()
                items["tag"]=item.css("div.tags a.tag::text").getall()
                yield items



"""
import scrapy
class quots(scrapy.Spider):
	name="sp"
	start_urls=["https://quotes.toscrape.com/"]
	def parse(self, response):
		for item in response.css("div.quote"):
			yield {
				"text":  item.css("span.text::text").get(),
				"author":item.css("small.author::text").get(),
				"tag":item.css("div.tags a.tag::text").getall()
			    }
		next_page=response.css("li.next a::attr(href)").get()
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)
			
			"""