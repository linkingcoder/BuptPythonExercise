t = int(input())
for x in range(t):
    words = list(input().split(' '))
    for i in range(len(words)):
        words[i] = words[i].lower()
        if len(words[i]) <= 4:
            word = words[i]
        else:
            word = words[i][:4]+'.'
        if i != len(words)-1:
            print(word, end=' ')
        else:
            print(word)
