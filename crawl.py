#Importing the scrapy library
import scrapy

from scrapy.crawler import CrawlerProcess

#creating our crawler class
class Crawler(scrapy.Spider):
  name = "Quote_Crawler" #our crawler's name
  start_urls = [
   # "http://quotes.toscrape.com/", #the url to be crawled
   # "http://quotes.toscrape.com/page/2/"
   "https://en.wikipedia.org/wiki/Cheetos"
  ]

  
  def parse(self, response):
    #for item in response.css('div.mw-body-content'):
    yield {
        #"quote" : item.css(".text::text").extract_first(),
        #"author" : item.css(".author::text").extract_first()
        "Text: " : response.css("a::attr(href)").extract_first()
      }
      
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(Crawler)
process.start() # the script will block here until the crawling is finished
