"""
There are 10 kinds of those kind of binary, those that understand binary and those who don't.
"""
import os

# os.system('cls' if os.name == 'nt' else 'clear')
cc_num = '4556737586899855'  # input('Enter 16-digit credit card number:\n')
# why does line 5 have to exsist?
# print()
# print(cc_num)
# print(type(cc_num))
cc_num = list(cc_num)

# # new_cc_num = []
# # for x in cc_num:
# #     new_cc_num.append(x)
# # cc_num = new_cc_num
#
# print()
# print(cc_num)
# print(type(cc_num))
#
# cc_num = ''.join(cc_num)
#
# print()
# print(cc_num)
# print(type(cc_num))
# print(cc_num)
#


# did this line flip the code of the list?
check_digit = cc_num[-1]
# print(check_digit)

# or did this line flip the code of the list?
# print(cc_num)
new_cc1 = cc_num[:-1]
# print(new_cc1)
# """
# what is the differencr between reverse(list)
# list.reverse() and  and where do you use which?
# """
new_cc1.reverse()
# print(new_cc1)

# I thought this was just a blank list
new_cc2 = []  # [int(new_cc1[foo])*2 if foo % 2 == 0 else int(new_cc1[foo]) for foo in range(len(new_cc1))]
# print(new_cc2)
# is num was a variable or is it a call out to something
for foo in range(len(new_cc1)):
    # no idea what is happening here.
    if foo % 2 == 0:
        # I have no idea what this is suppose to mean or how to translate it
        new_cc2.append(int(new_cc1[foo]) * 2)

    # """
    # Something isnt getting multiplied by 2 no idea what it by
    # looking at the code.
    # know from class but NOT BY READING it
    # """
    else:
        new_cc2.append(int(new_cc1[foo]))

print(new_cc2)
# another blank list
new_cc3 = []

for num in new_cc2:
    # """
    # #still no idea what is happening here other than if
    # xxx is greater than 9. The rest might as well be noise
    # line 50 seems errelivant... so that means that num 3 and num 2
    # are different but i don't know how.
    # """
    # if num2 > 9:
    #    num3 = (num2 - 9)
    #    new_cc3.append(num3)
    # else:
    #    new_cc3.append(num2)
    if num > 9:
        new_cc3.append(num - 9)
    else:
        new_cc3.append(num)

print(new_cc3)
#
# print(new_cc3)
#
new_cc3 = sum(new_cc3)
print(new_cc3)
# """
# # im begining to question whether or not I
# know what the difference between stringas and list
# """
new_cc3 = str(new_cc3)
new_cc3 = list(new_cc3)
#
if check_digit == new_cc3[1]:
    # this means it worked
    print('Valid!')
    # if it didnt work then print this line... THIS IS THE ONLYTHING THAT MADE SINCE
else:
    print('Invalid!')
