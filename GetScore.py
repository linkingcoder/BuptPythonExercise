l = list(input().split())
sum = 0
x = 0
for i in l:
    i = eval(i)
    l[x] = i
    x += 1
    sum += i
high = max(l)
low = min(l)
avg = (sum - high - low) / (len(l) - 2)
print("最高分:%.2f" % high)
print("最低分:%.2f" % low)
print("平均分:%.2f" % avg)
