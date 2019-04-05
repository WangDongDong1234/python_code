"""
有N条绳子，他们的长度分别是Li.如果从它们中切割K条长度相同的绳子的话，这k条绳子每条最长能有多少
N=4
K=11
8.02,7.43,4.57,5.39
"""
n=int(input())
k=int(input())
length_str=input().strip()
length=[float(item) for item in length_str.split(',')]

def check(x):
    total=0
    for item in length:
        total+=int(item/x)
    return total>=k

if __name__=='__main__':
    max_length=int(max(length))+1
    min_length=0
    while max_length-min_length>1:
        mid=int((min_length+max_length)/2)
        if check(mid):
            min_length=mid
        else:
            max_length=mid
    print(max_length)
