import scrapy

from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from ..items import SparItem
from itemloaders.processors import TakeFirst


class SparSpider(scrapy.Spider):
	name = 'spar'
	start_urls = ['https://www.spar.is/is/um-sparisjodinn/frettir']

	def parse(self, response):
		post_links = response.xpath('//h2/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="stepper next"]/@href')
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//div[@id="news"]/div/h1/text()').get()
		description = response.xpath('//div[@class="entryContent"]/descendant-or-self::*/text()[normalize-space() and not(self::a | self::img)]').getall()
		description = ' '.join(description)
		date = response.xpath('//div[@class="entryInfo"]/span/text()').get()

		item = ItemLoader(item=SparItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()