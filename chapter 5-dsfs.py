# -*- coding: utf-8 -*-
"""
==========STATISTICS=============
"""

from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25,
               # ... and lots more
              ]

friend_counts = Counter(num_friends)
xs = range(101)                         # largest value is 100
ys = [friend_counts[x] for x in xs]     # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)
print("No of People",num_points)

largest_value = max(num_friends)            # 100
smallest_value = min(num_friends) 
print("Max friend of an individual",largest_value)
print("Min friends of an individual", smallest_value)

"""
Central Tendencies
* usually we consider mean 
================MEAN====================
mean is simply the average
"""

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

print(mean(num_friends))   # 7.333333

"""
============MEDIAN=================
median is the middle most number
* if the length of a sequence is n and its odd then median is 
  (n+1)/2 position in the sorted sequence.
* If the length of the sequence is even then median is n/2 postion in
  the sequence.(We also might take the average of n/2 and n/2+1 when it has even length)
"""
