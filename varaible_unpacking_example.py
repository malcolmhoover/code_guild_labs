import random

# Ask the user for three adjectives
adjectives = input('Give me three adjectives to describe a cat, separated by a comma: ')

# Split the adjectives into a list separated by a comma and print the list
x = adjectives.split(", ")


# Shuffle using random
random.shuffle(x)
print(x)
# Assign three variables to x
ad1, ad2, ad3 = x
ad1 = int(ad1)
ad1 += 1
print('ad1 is now: {}'.format(ad1))
# print("The cat is "+ str(ad1) + ", " + x[1] + "," + x[2] + ".")
print("The cat is {}, {}, and {}.".format(ad1, ad2, ad3))
