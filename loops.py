# import time
# import os
# clr = os.system
# hours = list(range(1, 13))
# minutes = list(range(0, 60))
# mil = list(range(0, 10))
# print(hours)
#
# while True:
#     for h in hours:
#         h = '{}'.format('0'+ str(h) if len(str(h)) < 2 else h)
#         print('{}'.format(h))
#         for m in minutes:
#             m = '{}'.format('0'+ str(m) if len(str(m)) < 2 else m)
#             for s in minutes:
#                 s = '{}'.format('0'+ str(s) if len(str(s)) < 2 else s)
#                 clr('clear')
#                 print('{}:{}:{}'.format(h, m, s))
#                 time.sleep(1)

# number = 0
# while number <= 1000:
#     print('Hello! #{}'.format(number))
#     number += 1


# froot = ['apple', 'banananana', 'orange', 'kiwi', 'food', 'some', 'other', 'food', 'stuff']
# print(froot)
# time.sleep(2)
# froot[1] = 'banana'
# print('fixed banana:')
# print(froot)
# time.sleep(2)
# froot.append('grapes')
# print('added grapes:')
# print(froot)
# time.sleep(2)
# print('start for loop:')
# iteration_number = 0
# for f in froot:
#     print('Iteration #{}'.format(iteration_number))
#     iteration_number += 1
#     print('f = {}'.format(f))
#     print('popping last item from froot:')
#     froot.pop()
#     print(froot)
#     time.sleep(2)

number_die = input('How many die would you like to roll?: ')

for d in range(int(number_die)):
    print('something')
