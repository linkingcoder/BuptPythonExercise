t = int(input())
for i in range(t):
    team_list = {}
    com_list = input().split(' ')
    n = int(com_list[0])
    ms = com_list[1]
    for j in range(n):
        team = input().split(' ')
        name = team[0]
        m = int(team[1])
        g = int(team[2])
        team_list[name] = (m, g);
    res = sorted(team_list.items(),key=lambda x: (x[1][0], x[1][1]))
    cnt = 0
    for r in res:
        if r[0] == ms:
            break;
        cnt += 1
    if cnt <= round(n*0.6):
        print('YES')
    else:
        print('NO')
