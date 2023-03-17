from collections import Counter
import random

lst = []
for i in range(10000000):
    lst.append(random.randint(1, 6))
print(Counter(lst))




