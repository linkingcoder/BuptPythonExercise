import pandas as pd
df = pd.read_csv('BeijingPM20100101_20151231.csv',encoding='utf-8')
# 对HUMI、PRES、TEMP三列，进行线性插值处理。
df['HUMI'] = df['HUMI'].interpolate()
df['PRES'] = df['PRES'].interpolate()
df['TEMP'] = df['TEMP'].interpolate()
# 修改cbwd列中值为“cv”的单元格，其值用后项数据填充。
for i in range(len(df['cbwd'])):
    if df['cbwd'][i] =='cv':
        df['cbwd'][i] = df['cbwd'][i+1]
    else:
        pass
df.to_csv("PM_BJ.csv",index=False)


