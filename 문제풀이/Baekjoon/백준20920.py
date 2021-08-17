# -*- coding: utf-8 -*-
"""백준20920

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kCnk4yAeXWpIChK9xlX86I2J-dbD3a2n
"""

# 영단어 암기는 괴로워
import sys

words = {}
N, M = map(int, input().split())
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for i in sorted(words, key=lambda x:(-words[x],-len(x),x)): # lambda에서 '-'가 reverse=True 역할
    if len(i) >= M:
        print(i)