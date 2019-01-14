"""
8 5 8
"""
import copy
reuqire_str=input().strip()
require=[int(item) for item in reuqire_str.split(" ")]
require.sort(reverse=True)

i=len(require)-1
spend=0
while i>0:#合并成最后一个
    first=require.pop()
    i-=1
    second=require.pop()
    i-=1
    total=first+second
    spend+=total
    require.append(total)
    i+=1
    require.sort(reverse=True)
print(spend)

