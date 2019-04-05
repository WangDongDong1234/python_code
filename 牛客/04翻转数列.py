"""
小Q定义了一种数列称为翻转数列:
给定整数n和m, 满足n能被2m整除。对于一串连续递增整数数列1, 2, 3, 4..., 每隔m个符号翻转一次, 最初符号为'-';。
例如n = 8, m = 2, 数列就是: -1, -2, +3, +4, -5, -6, +7, +8.
而n = 4, m = 1, 数列就是: -1, +2, -3, + 4.
小Q现在希望你能帮他算算前n项和为多少。
"""
n_m_str=input().strip()
n_m=[int(item) for item in n_m_str.split(' ')]
n=n_m[0]
m=n_m[1]
print(int((n/(2*m))*(m**2)))
# array=[-i for i in range(1,n+1)]
# for i in range(1,len(array)+1):
#     if i%(2*m)==0:
#         for j in range(m):
#             array[i-j-1]=0-array[i-j-1]

#print(sum(array))
array=[-i for i in range(1,n+1)]
#print(array)
book=False
count=0
for i in range(1,len(array)+1):
    if book:
        array[i-1]=0-array[i-1]
    count+=1
    if count%m==0:
        if book==False:
            book=True
        else:
            book=False
        count = 0

print(sum(array))





