def acronym(phrase):
    words = list(phrase.split())
    res=''
    for word in words:
        word = word.upper()
        res = res+word[0]
    return res

phrase=input()
print(acronym(phrase))