from lxml import etree
import urllib.request
import json

base_url = 'https://bj.lianjia.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 118.0.0.0Safari / 537.36',
}
region = ['dongcheng/', 'xicheng/', 'chaoyang/', 'haidian/']
pages = ['', 'pg2/', 'pg3/', 'pg4/', 'pg5/']
# 创建一个列表用于存储所有数据
all_data = []
for i in region:
    temp = base_url + i
    for j in pages:
        url = temp + j
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # 解析服务器响应文件
        tree = etree.HTML(content)
        name =tree.xpath('//*[@id="content"]/div/ul/li/div[1]/div[1]/a/text()')
        address =tree.xpath('//*[@id="content"]/div/ul/li/div[1]/div[2]/div/a[2]/text()')
        space =tree.xpath('//*[@id="content"]/div/ul/li/div[1]/div[3]/div/text()')
        totalprice =tree.xpath('//*[@id="content"]/div/ul/li/div[1]/div[6]/div[1]/span/text()')
        singleprice =tree.xpath('//*[@id="content"]/div/ul/li/div[1]/div[6]/div[2]/span/text()')
        for (a, b, c, d) in zip(name, totalprice, space,singleprice):
            data = {'楼盘名称': a, '总价': b, '其他': c, '单价':d + '万'}
            all_data.append(data)
# 在循环结束后，打开文件并将所有数据写入
with open('house.json', 'a', encoding='utf-8') as fp:
    json.dump(all_data, fp, ensure_ascii=False, indent=2)
