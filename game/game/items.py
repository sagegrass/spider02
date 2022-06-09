import scrapy


class GameItem(scrapy.Item):
    name = scrapy.Field()
    publish_time = scrapy.Field()
    type = scrapy.Field()
    producer = scrapy.Field()
    info = scrapy.Field()
    collection = scrapy.Field()

