import re
import pymongo


class CleanItemPipeline:
    def process_item(self, item, spider):
        item["publish_time"] = item["publish_time"].replace("发行日期：", "")
        item["producer"] = item["producer"].replace("制作发行：  ", "")
        item["info"] = re.sub("\s", "", item["info"])
        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        collection = item["collection"]
        mongo_item = {}
        mongo_item["name"] = item["name"]
        mongo_item["publish_time"] = item["publish_time"]
        mongo_item["type"] = item["type"]
        mongo_item["producer"] = item["producer"]
        mongo_item["info"] = item["info"]
        self.db[collection].insert_one(mongo_item)
        return item

    def close_spider(self, spider):
        self.client.close()



