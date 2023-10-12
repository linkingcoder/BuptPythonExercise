n = input()
if len(n) <= 8:
    print('invalid password')
else:
    l = 0
    n = 0
    o = 0
    for i in n:
        if '0' <= i <= '9':
            n = n + 1
        elif 'a' <= i <= 'z' and 'A' <= i <= 'Z':
            l = l + 1
        else:
            o = o + 1
    if l == 0 or o == 0 or n == 0:
        print('invalid password')
    else:
        print('valid password')



