from math import sin, radians, cos

from dda import dda
from wu import wu

# print(wu(-200,200,200,-200))
# print(wu(-200,-200,200,100))
# print(wu(370.5, 565.5, 770.5, 265.5))

# print(dda(-200,200,200,-200))
# print(dda(-200,-200,200,100))
# print(dda(370.5, 565.5, 770.5, 265.5))

angle = 327
r = 300

x = 368.98355704444003
y = 55.19188986019313

angle = 0
center_x = center_y = 0
while angle < 360:
    x = sin(radians(angle)) * r
    y = cos(radians(angle)) * r

    pix1 = dda(0, 0, x, y)
    pix2 = wu(0, 0, x, y)


    for i in range(min(len(pix1), len(pix2))):
        if pix1[i][0] != pix2[i][0] or pix1[i][1] != pix2[i][1]:
            print(angle)

    angle += 3