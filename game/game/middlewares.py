from scrapy.exceptions import IgnoreRequest


class StopSpiderDownloaderMiddleware:

    def process_response(self, request, response, spider):
        if request.url.endswith(".jpg"):
            return response
        game_count = len(response.xpath("//li[@class='lx1']"))
        if not game_count:
            raise IgnoreRequest("已经结束了")
        else:
            return response
