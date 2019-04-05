"""
小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力
思路   有问题
100 382
114

我的代码输出是145
"""
n_m_str=input().strip()
n_m=[int(item) for item in n_m_str.split(' ')]
n=n_m[0]
m=n_m[1]
#第一天最多吃的个数,求出总共的
def eat(num):
    sum=0
    for i in range(n):
        sum+=num
        num=(num+1)//2
    return sum

def fun(m):
    i=1
    j=m
    while i<j:
        if n==1:
            return m
        mid=(i+j)//2
        if eat(mid)==m:
            return mid
        elif eat(mid)<m:
            i=mid+1
        else:
            j=mid-1
    return i
print(fun(m))


"""

# -*- coding:utf-8 -*-

#python3
n,m=[int(i) for i in input().split()] #出差n天，m块巧克力

#计算第一天吃s个巧克力一共需要多少个巧克力
def my_sum(s):
    total_sum=0
    for i in range(n):
        total_sum+=s
        s=(s+1)//2  #向上取整
    return total_sum

low, high = 1, m  # 第一天吃的巧克力一定是大于等于1，小于等于m的
while(low<=high):
    mid=(low+high)//2
    if my_sum(mid) == m:  # 如果第一天吃mid个巧克力，刚刚好吃完所有巧克力，那么直接返回
        print(mid)
        break
    elif my_sum(mid)<m:
        low=mid+1
    else:
        high=mid-1

if low>high:
    print(low-1)
"""