BOT_NAME = "game"

SPIDER_MODULES = ["game.spiders"]
NEWSPIDER_MODULE = "game.spiders"

USER_AGENT = "Mozilla/5.0"

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
   "game.middlewares.StopSpiderDownloaderMiddleware": 543,
}

MONGO_URI = "localhost"
MONGO_DB = "game"

ITEM_PIPELINES = {
   "game.pipelines.CleanItemPipeline": 301,
   "game.pipelines.MongoPipeline": 302
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1
