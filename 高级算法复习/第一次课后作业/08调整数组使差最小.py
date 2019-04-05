"""
Description

有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序； 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的
和]之间的差最小。题目不一定要用动态规划的方法，可以尝试其他方法，本题答案有多种，可以得到任意一种答案的方案都可以。
思考：可以尝试获得交换的次数，对比不同方案的交换次数和最终差值。
Input
输入为两行，分别为两个数组，每个值用空格隔开。
Output
输出变化之后的两个数组内元素和的差绝对值。
Sample Input 1
100 99 98 1 2 3
1 2 3 4 5 40
Sample Output 1
48
"""
a_str=input().strip()
b_str=input().strip()
a=[int(item) for item in a_str.split(" ")]
b=[int(item) for item in b_str.split(" ")]
cha=abs(sum(a)-sum(b))
for i in range(len(a)):
    for j in range(len(b)):
        a[i],b[j]=b[j],a[i]
        if(abs(sum(a)-sum(b))<cha):
            cha=abs(sum(a)-sum(b))
        else:
            a[i], b[j] = b[j], a[i]
print(a,b)
print("方案一",cha)
a.extend(b)

a.sort()

tmp_a=[]
tmp_b=[]
i=0
j=len(a)-1
print(a)
tmp_a.append(a[i])
tmp_b.append(a[j])
i=i+1
j=j-1
while j-i>=1:
    if sum(tmp_a)<sum(tmp_b):
        tmp_a.append(a[j])
        tmp_b.append(a[i])
    else:
        tmp_a.append(a[i])
        tmp_b.append(a[j])
    i+=1
    j-=1
print(tmp_a,tmp_b)
print(abs(sum(tmp_a)-sum(tmp_b)))


