# -*- coding: utf-8 -*-
"""백준2193

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RF_vsToO3qSX9Npn2U9fhciec_rYydJN
"""

# 이친수

n = int(input())
cnt = 0
a = [0,1]

for i in range(n):
    a.append(a[i] + a[i+1])

print(a[n])