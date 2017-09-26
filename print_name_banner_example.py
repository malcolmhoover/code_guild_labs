name = input ("Hello! What's your name?: ")
num = input("How old are you?: ")
num2 = int(num) + 1
filler_length = 120 - len(name)
filler = '*' * (filler_length // 2)
name_len = len(name)
if name_len % 2 != 0:
    name += '*'
# print('*' * len('name') + name + '*' * len('name'))
print('*' * (filler_length + name_len))
print('{0}{1}{0}'.format(filler, name))
print('*' * (filler_length + name_len))
print("{}, you will be {} in one year! ".format(name.replace('*', ''), num2))
