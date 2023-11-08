import pickle

with open('object.dat', 'rb') as fileload:
    obj1 = pickle.load(fileload)
    obj2 = pickle.load(fileload)
print(str(obj1))
print(str(obj2))
obj2[1]['score']['语文'] = 100
obj2[1]['name'] = '李四'
with open('object.dat', 'wb') as filesave:
    pickle.dump(obj1, filesave)
    pickle.dump(obj2, filesave)
print(str(obj1))
print(str(obj2))
