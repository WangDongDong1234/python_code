"""
小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。
01背包问题
"""
n=int(input())
array_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
array.sort(reverse=True)
a=[]
b=[]
for i in range(1,n+1):
    if i%2==0:
        a.append(array[i-1])
    else:
        b.append(array[i-1])

print(abs(sum(a)-sum(b)))
