import time
T1 = time.time()
fp = open('test6.txt', 'w')
for i in range(1000):
    fp.write('Hello Python!\n')
T2 = time.time()
print(T2-T1)
fp.close()

