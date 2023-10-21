s = ''
wordnum = {}
id = {'!', '.', ':', '*', '?', '#', ','}


def strreplace(s):
    for i in range(len(s)):
        if s[i] in id or '0' <= s[i] <= '9':
            s = s.replace(s[i], ' ')
    return s


while True:
    s = input()
    if s == '%%%':
        break
    s = strreplace(s)
    words = s.split()
    for w in words:
        w = w.strip().lower()
        if w in wordnum:
            wordnum[w] += 1
        else:
            wordnum[w] = 1

dic = sorted(wordnum.items(), key=lambda x: (-x[1], x[0]))
if len(dic) != 0:
    cnt = 0;
    print(len(dic))
    for k, v in dic:
        if cnt <= 5:
            print('%s=%d' % (k, v))
            cnt = cnt + 1
else:
    print('0')
