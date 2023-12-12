import numpy as np
# 0-50 优
# 51- 100 良
# 101 - 150 轻度污染
# 151 - 200 中度污染
# 201 - 300 重度污染
# >300      严重污染
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def PrintPlot(data,name):
    # 设置绘图风格
    plt.style.use('ggplot')
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 绘制散点图
    plt.scatter(x=df['No'],  # 指定散点图的x轴数据
                y=data,  # 指定散点图的y轴数据
                color='steelblue'  # 指定散点图中点的颜色
                )
    # 添加x轴和y轴标签
    plt.xlabel('编号')
    plt.ylabel(name)
    # 添加标题
    plt.title('关系')
    # 显示图形
    plt.show()


df = pd.read_csv('BeijingPM20100101_20151231.csv')
df['PM_Dongsi'] = [min(i, 500) for i in df['PM_Dongsi']]
df['PM_Dongsihuan'] = [min(i, 500) for i in df['PM_Dongsihuan']]
df['PM_Nongzhanguan'] = [min(i, 500) for i in df['PM_Nongzhanguan']]
MinMax_PRES = MinMaxScaler().fit_transform(df['PRES'].values.reshape(-1, 1))
MinMax_TEMP = MinMaxScaler().fit_transform(df['TEMP'].values.reshape(-1, 1))
Standard_PRES = StandardScaler().fit_transform(df['PRES'].values.reshape(-1, 1))
Standard_TEMP = StandardScaler().fit_transform(df['TEMP'].values.reshape(-1, 1))
PrintPlot(MinMax_PRES,'MinMax_PRES')
PrintPlot(MinMax_TEMP,'MinMax_TEMP')
PrintPlot(Standard_PRES,'Standard_PRES')
PrintPlot(Standard_TEMP,'Standard_TEMP')
best = good = low = middle = high = worst = 0
sumlist =[]
num_elements = len(df['PM_Dongsi'])
num_per_chunk = 24

# 将每列的数据均分为多个 chunk，每个 chunk 包含 24 个元素
chunks_dongsi = [df['PM_Dongsi'][i:i+num_per_chunk] for i in range(0, num_elements, num_per_chunk)]
chunks_dongsihuan = [df['PM_Dongsihuan'][i:i+num_per_chunk] for i in range(0, num_elements, num_per_chunk)]
chunks_nongzhanguan = [df['PM_Nongzhanguan'][i:i+num_per_chunk] for i in range(0, num_elements, num_per_chunk)]
for(x,y,z) in zip(chunks_nongzhanguan,chunks_dongsi,chunks_dongsihuan):
    # 在计算均值之前检查 NaN 值
    if x.isnull().values.any() or y.isnull().values.any() or z.isnull().values.any():
        continue  # 如果任何 NaN 值存在，则跳过处理
    daily_avg = (np.mean(x)+np.mean(y)+np.mean(z))/3
    sumlist.append(daily_avg)
    if 0 <= daily_avg <= 50:
        best += 1
    elif 51 <= daily_avg <= 100:
        good += 1
    elif 101 <= daily_avg <= 150:
        low += 1
    elif 151 <= daily_avg <= 200:
        middle += 1
    elif 201 <= daily_avg <= 300:
        high += 1
    elif daily_avg > 300:
        worst += 1
print(best)
print(good)
print(low)
print(middle)
print(high)
print(worst)
