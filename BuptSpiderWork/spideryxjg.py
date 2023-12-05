from lxml import etree
import urllib.request

url = 'https://www.bupt.edu.cn/yxjg1.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 解析服务器响应文件
tree = etree.HTML(content)
names = tree.xpath('//div[@class="center news"]/div/ul/li/div/ul/li/a/text()')
hrefs = tree.xpath('//div[@class="center news"]/div/ul/li/div/ul/li/a/@href')
t = dict(zip(names, hrefs))
with open('yxjg.txt', 'w', encoding='utf-8') as fp:
    for (name, href) in t.items():
        fp.write('name:' + name + ' ' + 'href:' + href)
        fp.write('\n')
