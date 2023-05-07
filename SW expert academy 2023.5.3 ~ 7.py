#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2023 5 3
# 369

a = int(input())

for i in range(1,a+1):
    if i%3 == 0:
        print("-", end = " ")
    else:
        print(i, end = " ")


# In[ ]:


# 2023 5 3
# 회문
# palindrome


def palin(word):
    if len(word) <= 1:
        return True
    else:
        return (word[0] == word[-1]) and palin(word[1:-1])

T = int(input())

for i in range(1,T+1):
    a = input()
    if palin(a):
        print("#%d %d"%(i, 1))
    else:
        print("#%d %d"%(i, 0))


# In[ ]:


# 2023 5 3
# 지그재그 숫자
# zigzag


a = int(input())

for i in range(1, a+1):
    s = 0
    b = int(input())
    for j in range(1, b+1):
        if j%2 !=0:
            s += j
        else:
            s -= j
    print("#%d %d"%(i, s))


# In[ ]:


# 2023 5 4
# average except first and last one.



def turn_to_int(a):
    for i in range(len(a)):
        a[i] = int(a[i])


l = int(input())



for l in range(1, l+1):
    a = input().split()
    turn_to_int(a)
    for j in range(len(a)):
        k = len(a) - j
        for i in range(1, k):
            if a[i-1] >= a[i]:
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
    b = a[1:-1]
    c = 0
    for j in range(len(b)):
        c += b[j]
    print("#%d %.0f"%(l, round(c/len(b),1)))


# In[ ]:


# 2023 5 5
# 최빈값 구하기
# frequency

import sys


def freq(data):
    freq_dict = {}
    for j in data:
        if j in freq_dict:
            freq_dict[j] +=1
        else:
            freq_dict[j] = 1
    return freq_dict

def turn_to_int(c):
    for i in range(len(c)):
        c[i] = int(c[i])

T = int(input())

for i in range(1,T+1):
    a = int(input())
    c = input().split()
    turn_to_int(c)
    b = freq(c)
    max_num = max(b, key=lambda k: b[k])
    print("#%d %d"%(a, max_num))


# In[ ]:


# 2023 5 5
# 격자점
# grid point


import math

T = int(input())


def grid_points(radius):
    count = 0
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if math.sqrt(x**2 + y**2) <= radius:
                count += 1
    return count



for i in range(1, T+1):
    radius = int(input())
    count = grid_points(radius)
    print("#%d %d"%(i, count))


# In[1]:


# 2023 5 6
# 조망권 찾기



for l in range(1, 11):
    r = int(input())
    b = list(map(int, input().split()))
    c = 0
    # two of left and right sides are empty.
    for i in range(2, r-2):
        # find the highest building
        m = max(b[i+1], b[i+2], b[i-1], b[i-2])
        if b[i] - m > 0 : c += b[i] - m
    print("#{} {}".format(l, c))
    
    
    

