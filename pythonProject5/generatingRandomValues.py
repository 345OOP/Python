# generating Random Values

import random
# example1
# for i in range(3):
#     print(random.random())
#     print(random.randint(10,20))

# example2
# members = ['John', 'Mary', 'Lois', 'Clark']
# leader = random.choice(members)
# print(leader)

# example Dice


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first,second


dice = Dice()
print(dice.roll())