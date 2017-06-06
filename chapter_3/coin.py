import random

eagle = 0
tail = 0
count = 0

while count != 100:
    throw = random.randint(0, 1)
    if throw == 0:
        eagle += 1
    else:
        tail += 1
    count += 1

print("The eagle fell out ", eagle, " times",
      "\nThe tail fell out ", tail, " times")
