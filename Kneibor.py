K = int(input())
T = int(input())
L = list(input().split())
indexs = {}
cnt = 0
# 将距离作为键，索引作为值存入字典
for i in range(len(L)):
    num = int(L[i])
    dis = abs(num - T)
    indexs[i] = dis
# 按距离对字典进行排序，并获取前K个最小距离的索引
sorted_indices = sorted(indexs, key=indexs.get)[:K]
# 打印前K个最接近的值的索引
for index in sorted_indices:
    print(index, end=" ")
