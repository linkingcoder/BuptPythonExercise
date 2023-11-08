import csv

sum = 0
data = []
with open('num.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
# 解析csv
headers = data[0]
rows = data[1:]
# 求和
for i in rows:
    sum += int(i[1])
print(sum)