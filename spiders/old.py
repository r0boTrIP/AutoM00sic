#!/usr/bin/env python3
import scrapy

queue = [] 

class SoundcloudSpider(scrapy.Spider):
	name = "soundcloud"

	allowed_domains = ['soundcloud.com']

	start_urls = [queue]

	def parse(self, response):
		self.logger.info("test")
		pass

