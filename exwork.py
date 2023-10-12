s = input()
f = 0
for i in range(1, len(s)):
    a = ord(s[i-1])
    b = ord(s[i])
    if 'A' <= s[i-1] <= 'Z':
        if (b == a-1) or (b == a+32):
            f = f+1
    else:
        if (b == a+1) or (b == a-32):
            f = 1+f
if f == len(s)-1:
    print('Y')
else:
    print('N')