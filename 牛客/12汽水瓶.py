# def fun(n):
#     global count
#     if n<=1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return n//3+fun(n%3+n//3)
#
# result=[]
# while 1:
#     n=int(input())
#     if n==0:
#         break
#     else:
#         count=fun(n)
#         result.append(count)
#
# for item in result:
#     print(item)

"""
找规律
"""
while 1:
    n=int(input())
    if n==0:
        break
    else:
        print(n//2)
