#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2023 04 24
# 홀수만 더하기
# Add only odd numbers


T = int(input())

def turn_to_int(a):
    for i in range(len(a)):
        a[i] = int(a[i])


def odd(a):
    b = 0
    for num in a:
        if num%2 != 0:
            b += num
    return b


for test_case in range(1, T+1):
    a = input().split()
    turn_to_int(a)
    b = odd(a)
    print('#%d %d'%(test_case, b))


# In[ ]:


# 2023 04 25
# 평균 구하기
# Average


T = int(input())

def turn_to_int(a):
    for i in range(len(a)):
        a[i] = float(a[i])


def average(a):
    b = 0
    for num in a:
        b += num
    return round(b/len(a))


for test_case in range(1, T+1):
    a = input().split()
    turn_to_int(a)
    b = average(a)
    print('#%d %d'%(test_case, b))


# In[ ]:


# 2023 04 25
# 최대수 구하기
# biggest number


T = int(input())

def turn_to_int(a):
    for i in range(len(a)):
        a[i] = float(a[i])


def the_big(a):
    max = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            if max < a[i+1]:
                max = a[i+1]
        else:
            if max < a[i]:
                max = a[i]
    return max

for test_case in range(1, T+1):
    a = input().split()
    turn_to_int(a)
    max = the_big(a)
    print("#%d %d"%(test_case, max))


# In[ ]:


# 2023 04 25
# 중간값 구하기
# median



def turn_to_int(a):
    for i in range(len(a)):
        a[i] = int(a[i])


l = int(input())

a = input().split()
turn_to_int(a)

for j in range(len(a)):
    k = len(a) - j
    for i in range(1, k):
        if a[i-1] >= a[i]:
            temp = a[i-1]
            a[i-1] = a[i]
            a[i] = temp

b = (l//2)
print(a[b])


# In[ ]:


# 2023 04 26
# 자리수 더하기
# sum each numbers


a = int(input())
b = 0
if a >= 1000:
    for i in range(4):
        if i == 0:
            b += a//1000
    elif i == 1:
        b += a%1000//100
    elif i == 2:
        b += a%100//10
    else:
        b += a%10/1
elif a >= 100:
    for i in range(3):
        if i == 0:
            b += a//100
        elif i == 2:
            b += a%100//10
        else:
            b += a%10//1
elif a >= 10:
    for i in range(2):
        if i == 0:
            b += a%100//10
        else:
            b += a%10//1
else:
    b = a

print(int(b))

