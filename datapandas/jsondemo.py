import pandas as pd
import numpy as np
def fund(listTemp, n):
    resules = []
    for i in range(0, len(listTemp), n):
        temp = listTemp[i:i + n]
        resules.append(temp)
    return resules
df = pd.read_json('house.json')
print(df)
totolpricelist = []
singlepricelist = []
before2000 = []
between2000and2009 = []
after2010 = []
totolprice = np.array(df['总价'])
singleprice = np.array(df['单价'])
info = np.array(df['其他'])
length = int(len(df) / 4)
for i in range(len(totolprice)):
    str = totolprice[i]
    totolpricelist.append(int(str))
for i in range(len(singleprice)):
    str = singleprice[i].replace(',', '')
    singlepricelist.append(int(str[:-4]))
singlepricelists = [singlepricelist[i:i + length] for i in range(0, len(singlepricelist), length)]
totolpricelists = [totolpricelist[i:i + length] for i in range(0, len(totolpricelist), length)]
print('东城平均总价%d万元，最高总价%d万元，最低总价%d万元' % (
    np.mean(totolpricelists[0]), np.max(totolpricelists[0]), np.min(totolpricelists[0])))
print('西城平均总价%d万元，最高总价%d万元，最低总价%d万元' % (
    np.mean(totolpricelists[1]), np.max(totolpricelists[1]), np.min(totolpricelists[1])))
print('朝阳平均总价%d万元，最高总价%d万元，最低总价%d万元' % (
    np.mean(totolpricelists[2]), np.max(totolpricelists[2]), np.min(totolpricelists[2])))
print('海淀平均总价%d万元，最高总价%d万元，最低总价%d万元' % (
    np.mean(totolpricelists[3]), np.max(totolpricelists[3]), np.min(totolpricelists[3])))
print('东城平均单价%d元/平方，最高单价%d元/平方，最低单价%d元/平方' % (
    np.mean(singlepricelists[0]), np.max(singlepricelists[0]), np.min(singlepricelists[0])))
print('西城平均单价%d元/平方，最高单价%d元/平方，最低单价%d元/平方' % (
    np.mean(singlepricelists[1]), np.max(singlepricelists[1]), np.min(singlepricelists[1])))
print('朝阳平均单价%d元/平方，最高单价%d元/平方，最低单价%d元/平方' % (
    np.mean(singlepricelists[2]), np.max(singlepricelists[2]), np.min(singlepricelists[2])))
print('海淀平均单价%d元/平方，最高单价%d元/平方，最低单价%d元/平方' % (
    np.mean(singlepricelists[3]), np.max(singlepricelists[3]), np.min(singlepricelists[3])))
for (i, j) in zip(info, singlepricelist):
    list = i.split('|')
    str = list[len(list) - 2].strip()[:-1]
    if len(str) == 4:
        year = int(str)
        if year < 2000:
            before2000.append(j)
        elif 2000 <= year <= 2009:
            between2000and2009.append(j)
        else:
            after2010.append(j)
print('---------------------------------------------')
print('2000年以前的平均单价:%d元/平方' % (np.mean(before2000)))
print('2000-2009.12.31的平均单价%d元/平方' % (np.mean(between2000and2009)))
print('2010-至今的平均单价%d元/平方' % (np.mean(after2010)))
