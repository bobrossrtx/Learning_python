# I want to make a random number generator

import random
from datetime import datetime 

dt = datetime(2018, 1, 1)
seed = int(round(dt.timestamp() * 10))
# print(random_number)

start_number = random.randint(1, 10)

random_number = round(start_number * seed / 1000)

if random_number > 0:
  print("Your random number is " + str(random_number))
elif random_number == start_number:
  print("Your random number is " + str(random_number))

length = len(str(random_number))
print(f"Your random number is {length} digits")