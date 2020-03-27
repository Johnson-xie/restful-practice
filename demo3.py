import random


lst = [random.randint(1, 30) for i in range(20)]
print(lst)

import heapq

heapq.heapify(lst)
print(lst)