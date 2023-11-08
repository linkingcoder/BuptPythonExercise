import csv
headers = ['编号', 'int']
with open('num.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for i in range(1000):
        rows = [str(i), i]
        writer.writerow(rows)