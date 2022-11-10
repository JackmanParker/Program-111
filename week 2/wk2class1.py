from ast import Num
import math
import random
from datetime import datetime

#print(round(int(input(len("1234567890123456789012345"))) / 25 )) 

#print("slkekn", "test", sep= "----", end= "\n", flush= True )

#finalnum = (math.ceil((17 ** 9) / 3) - 6) % 2

#if finalnum > 0:
#    even = False
#else:
#    even = True

#print(even)

#def random_math():
#    return (math.ceil(17 ** 9 / 3) -6) % 2 == 0

#print(random_math())
listed = []
for i in range(0,50):
    listed.append(random.randint(0, 100))

listed.sort(reverse=True)
print(listed)

now = datetime.now() 
print(now.minute % 2 == 0)

