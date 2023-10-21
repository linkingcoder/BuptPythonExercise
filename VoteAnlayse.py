vote = list(input().split(','))
team = ['6', '7', '8', '9', '10']
for i in vote:
    if i in team:
        team.remove(i)
for i in range(len(team)):
    if i!=len(team)-1:
        print(team[i], end=' ')
    else:
        print(team[i])



