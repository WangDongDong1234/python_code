"""
1
49 38 65 97 76 13 27 49 55 4
5 3
从第gap个开始每次gap确保gap前的排好序
"""
def shell_sort(list,gap):

    n=len(list)
    for i in range(gap,n):
        x=list[i]
        j=i
        while j>gap-1 and list[j-gap]>x:
            list[j],list[j-gap]=list[j-gap],list[j]
            j-=gap
    return list
num=int(input())
for i in range(num):
    array_str=input().strip()
    array=[int(item) for item in array_str.split(" ")]
    gap_str=input().strip()
    gaps=[int(item) for item in gap_str.split(" ")]
    for gap in gaps:
        array=shell_sort(array,gap)
    for i in range(len(array)):
        if i==0:
            print(array[i],end="")
        else:
            print("",array[i],end="")
    print()