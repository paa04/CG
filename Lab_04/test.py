from modules.algorithms.midpoint import *
from modules.algorithms.bresenham import *

s1 = set()
s2 = set()

for i in bresellipse(325.5, 325.5, 100, 50, [255, 255, 255]):
    s1.add(tuple(i[:2]))

for i in midpellipse(325.5, 325.5, 100, 50, [255, 255, 255]):
    s2.add(tuple(i[:2]))

print(s1)

print(s1 - s2)
print(s2 - s1)
