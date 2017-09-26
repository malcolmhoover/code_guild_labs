# NUMBER = 12
# snake_case = 6

# number = 'five'
# number = 5
# print(number)

# a = 1
# b = 2
# a = b
# b = 15
# a = b
# print(a)

# a, b = 1, 2
# a, b = b, a
#
# print(a)
# p = print
#
# p('this thing')

def pretty_print(x):
    return '({}) {}-{}'.format(x[:3], x[3:6], x[6:])

def something():
    phone1 = input('Phone Number?: ')
    phone2 = input('Phone Number?: ')

    print(pretty_print(phone1))
    print(pretty_print(phone2))


something()
