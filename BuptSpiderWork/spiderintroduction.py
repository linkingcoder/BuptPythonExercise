from lxml import etree
# 解析本地文件
tree = etree.parse('Introduction.html')
name = tree.xpath('//ul/li[@id="name"]/text()')
school = tree.xpath('//ul/li[@id="school"]/a/text()')
qqnumber = tree.xpath('//ul/li[@id="qq"]/text()')
home = tree.xpath('//ul/li[@id="home"]/text()')
print(name)
print(school)
print(qqnumber)
print(home)
