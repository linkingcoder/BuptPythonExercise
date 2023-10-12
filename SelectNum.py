s = input()
word = ''
list_res = []
for i in s:
    if ord('9') >= ord(i) >= ord('0'):
        word = word + i
    elif word:
        list_res.append(int(word))
        word = ''
if word:
    list_res.append(int(word))
print(len(list_res))
for l in range(len(list_res)):
    if l != len(list_res) - 1:
        print(list_res[l], end=" ")
    else:
        print(list_res[l])
