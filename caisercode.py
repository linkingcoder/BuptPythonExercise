def ReadEnglishWords():
    result = ['hello', 'world', 'you', 'me', 'like', 'i', 'python', 'this', \
              'is', 'are', 'the', 'great', 'so', 'thank', 'much', 'winter', 'summer']
    return result


def Decrypt(text, numToMove):
    afterText = ""
    for p in text:
        if ord("a") <= ord(p) <= ord("z"):
            afterText += chr(ord("z") - (ord('z') - ord(p) + numToMove) % 26)
        elif ord("A") <= ord(p) <= ord("Z"):
            afterText += chr(ord("Z") - (ord('Z') - ord(p) + numToMove) % 26)
        else:
            afterText += p
    return afterText


def Crack(text):
    words = text.split(' ')
    res = []
    for word in words:
        res.append(Decrypt(word, 12))
    return ' '.join(res)


t = input()
org = Crack(t)
print(org)
