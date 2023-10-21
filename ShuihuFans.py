data = []
while True:
    try:
        data = list(input().split(',')) + data
    except EOFError:
        break
dirt = {}
for name in data:
    name = name.strip()
    if name in dirt:
        dirt[name] += 1
    else:
        dirt[name] = 1
sorted_dirt = {k: v for k, v in sorted(dirt.items(), key=lambda item: item[1], reverse=True)}
for (key, value) in sorted_dirt.items():
    if len(key) != 0:
        print("%s:%d" % (key, value))