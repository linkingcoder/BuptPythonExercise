def isprimer(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
res = []
for x in range(2, n + 1):
    r = reversed(str(x))
    fn = ''.join(r)
    x2 = int(fn)
    if isprimer(x) and isprimer(x2) and x!=x2:
        res.append(x)
for i in range(len(res)):
    if i!=len(res)-1:
        print(res[i], end=' ')
    else:
        print(res[i], end='\n')