list_v = list(input().split(","))
res = 1
for i in list_v:
    res = int(i) * res
print(res)