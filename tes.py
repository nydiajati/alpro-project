# -*- coding: utf-8 -*-
"""
Nydia Lucyta Jati
Prodi Teknik Informatika
Jurusan Teknik Elektro

Created on %(date)

"""
import math

a = float(input("a (not nul)? "))
b = float(input("b? "))
c = float(input("c? "))
d = b**2-4*a*c
if d > 0:
    r0 = (-b-math.sqrt(d))/(2*a)
    r1 = (-b+math.sqrt(d))/(2*a)
    print(f"Two roots: {r0}, {r1}")
else:
    if d == 0:
        r = -b/(2*a)
        print(f"Single root: {r}")
    else:
        print("No root")
 