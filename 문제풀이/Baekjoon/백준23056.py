# -*- coding: utf-8 -*-
"""백준23056

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EGqHvxI14_LTGiJTmQsEAMZNOdnD55Za
"""

# 참가자 명단
import sys

N, M = map(int, input().split())
blue_team = {}   # 학급이 홀수
white_team = {}  # 학급이 짝수
while 1:
    cl, name = sys.stdin.readline().split()
    cl = int(cl)
    if cl == 0 and name == '0':
        break
    if cl % 2 == 1:
        if cl not in blue_team:
            blue_team[cl] = [name]
        else:
            if len(blue_team[cl]) < M:
                blue_team[cl].append(name)
    else:
        if cl not in white_team:
            white_team[cl] = [name]
        else:
            if len(white_team[cl]) < M:
                white_team[cl].append(name)

for i,v in sorted(blue_team.items()):
    for j in sorted(v, key=lambda x: (len(x), x)):
        print(i, j)
for i,v in sorted(white_team.items()):
    for j in sorted(v, key=lambda x: (len(x), x)):
        print(i, j)