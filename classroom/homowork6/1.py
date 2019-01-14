"""
给定一个数字的字符串“str”，找出“str”的最长子字符串的长度，这样子字符串的长度为2k位，左k位的和等于右k位的和。
"""
n=int(input())
r=[]
def solve():
    str = input().strip()
    str_list = []
    for item in str:
        str_list.append(int(item))
    length = len(str)
    max = 0
    start = 0
    while start < length - 1:
        for end in range(start + 1, length):
            if (end - start + 1) % 2 != 0:
                continue
            else:
                mid = int(start + (end - start) / 2)
                left = str_list[start:mid + 1]
                right = str_list[mid + 1:end + 1]
                if sum(left) == sum(right):
                    new_max = len(left)*2
                    if max < new_max:
                        max = new_max
                        # print(left,right)
        start += 1
    r.append(max)
for i in range(n):
    solve()
for item in r:
    print(item)