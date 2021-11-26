#!/usr/bin/env python3
import scrapy

class SoundcloudSpider(scrapy.Spider):
	name = "soundcloud"

	allowed_domains = ['soundcloud.com']

	start_urls = ["https://soundcloud.com"]

	def parse(self, response):
		self.logger.info("test")
		pass

