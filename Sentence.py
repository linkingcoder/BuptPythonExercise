class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
    def getSectence(self):
        return self.sentence
    def getWords(self):
        return list(self.sentence.split(" "))
    def getLength(self):
        return len(self.sentence)
    def getNumWords(self):
        return len(list(self.sentence.split(" ")))
    def setSentence(self):
        self.sentence = self.sentence.upper()
s = Sentence(input())
print('输入的字符串是：%s，共有%d个字符。'%(s.getSectence(),s.getLength()))
print('其中有单词：'+str(s.getWords())+'，共有%d个单词。'%s.getNumWords())
s.setSentence()
print('输入的字符串是：%s，共有%d个字符。'%(s.getSectence(),s.getLength()))
print('其中有单词：'+str(s.getWords())+'，共有%d个单词。'%s.getNumWords())
