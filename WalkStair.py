def fun(x):
    if x==1:
        return 1
    if x==2:
        return 2
    if x==3:
        return 4
    return fun(x-1)+fun(x-2)+fun(x-3)
n = int(input())
print(fun(n))