n = input()
num = '零壹贰叁肆伍陆柒捌玖'
units = ['亿', '仟万','佰万', '拾万', '万','仟','佰','拾','元']
integers = n[:-3]
chineseintegers=''
for i in range(len(integers)):
    print(i)
    chineseintegers = chineseintegers + num[int(integers[i])] + units[len(units)-len(integers)+i]
decimal = n[-3:]
chinesedecimal = num[int(decimal[1])]+'角'+num[int(decimal[2])]+'分'
print(chineseintegers + chinesedecimal)
