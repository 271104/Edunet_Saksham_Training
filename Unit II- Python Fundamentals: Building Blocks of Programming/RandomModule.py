import random

print(random.random())
toss = random.randint(0,1)
if toss == 0:
    print("It's Tails!")
else:
    print("It's Heads!")
    