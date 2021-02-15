# -*- coding: utf-8 -*-
"""백준1004

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qaYNB2s0OnRuAZByWvbz0ZpP3VagI2zZ
"""

T = int(input())

for i in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    for j in range(n):
        cx ,cy , r = map(int, input().split())
        dist1 = (x1-cx)**2 + (y1-cy)**2
        dist2 = (x2-cx)**2 + (y2-cy)**2
        
        if (dist1<r**2 and dist2>r**2) or (dist1>r**2 and dist2<r**2):
            count += 1
    print(count)