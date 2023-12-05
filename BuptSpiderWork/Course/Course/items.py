# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 课程名
    teacher = scrapy.Field()  # 老师
    school = scrapy.Field()  # 学校
    peopleNum = scrapy.Field()  # 选课人数
    pass
