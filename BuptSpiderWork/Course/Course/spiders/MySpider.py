import json
import scrapy

from ..items import CourseItem


class MyspiderSpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["xuetangx.com"]
    data = '{"query":"","chief_org":[],"classify":["1"],"selling_type":[],"status":[],"appid":10000}'
    url_base = 'https://www.xuetangx.com/api/v1/lms/get_product_list/?page={}'
    headers = {
        'Host': 'www.xuetangx.com',

        'authority': 'www.xuetangx.com',

        'method': 'POST',

        'path': '/api/v1/lms/get_product_list/?page=1',

        'scheme': 'https',

        'accept': 'application/json, text/plain, */*',

        'accept-encoding': 'gzip, deflate, br',

        'accept-language': 'zh',

        'content-type': 'application/json',

        'cookie': '_abfpc=9f1633a0e1b1086545423a2057a0fb7633573fd7_2.0; cna=6f8f375ae69d7aa2d320dede79ac329a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218bfb04e57425f-0cf11c4dd181708-26031051-1327104-18bfb04e575de7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22o.promote.cfjhyxft%22%2C%22%24latest_utm_campaign%22%3A%22%E4%B9%98%E9%A3%8E%E8%AE%A1%E5%88%921%E6%9C%9F%E9%A2%84%E6%8A%A5%E5%90%8D%E6%8E%A8%E5%B9%BF%22%7D%2C%22%24device_id%22%3A%2218bfb04e57425f-0cf11c4dd181708-26031051-1327104-18bfb04e575de7%22%7D; _gid=GA1.2.1773574411.1701169157; provider=xuetang; django_language=zh; point={%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}; _gat_gtag_UA_164784773_1=1; _ga=GA1.1.1694898043.1700723484; JG_016f5b1907c3bc045f8f48de1_PV=1701182154063|1701182154063; _ga_CP9FHE8ET4=GS1.1.1701182153.9.0.1701182162.0.0.0',

        'django-language': 'zh',

        'origin': 'https://www.xuetangx.com',

        'Referer': 'https: // www.xuetangx.com / search?query = & org = & classify = 1 & type = & status = & page = 1',

        'sec-fetch-dest': 'empty',

        'sec-fetch-mode': 'cors',

        'sec-fetch-site': 'same-origin',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

        'x-client': 'web',

        'xtbz': 'xt'

    }

    def start_requests(self):
        for page in range(1, 6):
            yield scrapy.FormRequest(
                url=self.url_base.format(page),
                headers=self.headers,
                method='POST',
                body=self.data,
                callback=self.parse
            )

    def parse(self, response):
        j = json.loads(response.body)
        for each in j['data']['product_list']:
            item = CourseItem()
            print(each['name'])
            item['name'] = each['name']
            item['school'] = each['org']['name']
            item['peopleNum'] = each['count']
            teacherList = []
            for teacher in each['teacher']:
                teacherList.append(teacher['name'])
                item['teacher'] = ','.join(teacherList)
            yield item
