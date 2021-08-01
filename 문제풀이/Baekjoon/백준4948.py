# -*- coding: utf-8 -*-
"""백준4948

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T6SIAWGYrxzN4S8xnq8CFNZAkXWQZHZP
"""

# 베르트랑 공준

N = 246912
is_prime = [False, False, True] + [True] * (N-2)
for i in range(2, N//2+1):
    if is_prime[i]:
        for j in range(2*i, N+1, i):
            is_prime[j] = False

n = int(input())
while n != 0:
    print(sum(is_prime[n+1:2*n+1]))
    n = int(input())