"""
5
1 2 4 6 8
3 5 7 9 10
"""
n=int(input())
start_str=input().strip()
start=[int(item) for item in start_str.split(" ")]
end_str=input().strip()
end=[int(item) for item in end_str.split(" ")]
result=[]
dict={}
for i in range(0,n):
    dict[end[i]]=start[i]
it=sorted(dict.items())
print(it)
start=0
total=0
for item in it:
    if item[1]>=start:
        start=item[0]
        total+=1
        print(item)

