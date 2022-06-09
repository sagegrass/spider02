import scrapy
from ..items import GameItem


class GameskySpider(scrapy.Spider):
    name = 'gamesky'
    allowed_domains = ['gamersky.com']
    base_url = "https://ku.gamersky.com"

    def start_requests(self):
        urls = {
            "pc": "https://ku.gamersky.com/release/pc_201701/",
            "ps5": "https://ku.gamersky.com/release/ps5_202101/",
            "ns": "https://ku.gamersky.com/release/switch_201801/",
            "xsx": "https://ku.gamersky.com/release/xsx_202101/",
            "ps4": "https://ku.gamersky.com/release/ps4_201701/"
        }

        for i in urls:
            yield scrapy.Request(
                url=urls[i],
                callback=self.parse,
                meta={"collection": i}
            )

    def parse(self, response):
        game = response.xpath("//li[@class='lx1']")
        item = GameItem()
        for i in game:
            item["name"] = i.xpath(".//div[@class='tit']/a/text()").extract_first()
            item["publish_time"] = i.xpath(".//div[@class='txt'][1]/text()").extract_first()
            item["type"] = i.xpath(".//div[@class='txt'][2]/a/text()").extract_first()
            item["producer"] = i.xpath(".//div[@class='txt'][3]/text()").extract_first()
            item["info"] = i.xpath(".//div[@class='Intr']/p/text()").extract_first()
            item["collection"] = response.meta["collection"]
            yield item
        if i := response.xpath("//a[text()='查看下一个月']/@href").extract_first():
            next_url = GameskySpider.base_url + i
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                meta={"collection": response.meta["collection"]}
            )

