# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
class CoursePipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open('StudyHallData.csv', 'w+', encoding='utf-8', newline='')
            self.csv = csv.writer(self.file)
        except Exception as e:
            print(e)
    def process_item(self, item, spider):
        self.csv.writerow(list(item.values()))
        return item
    def close_spider(self, spider):
        self.file.close()
