import random

# 生成1000行电话号码
phone_numbers = []

for _ in range(1000):
    # 生成随机的电话号码
    phone_number = '1'
    for _ in range(10):
        phone_number += str(random.randint(0, 9))

    phone_numbers.append(phone_number)

# 将电话号码保存到文件
with open('phone_numbers.txt', 'w') as file:
    for phone_number in phone_numbers:
        file.write(phone_number + '\n')

print("电话号码已保存到 phone_numbers.txt 文件")
