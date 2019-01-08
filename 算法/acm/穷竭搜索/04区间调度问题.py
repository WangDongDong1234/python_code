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
it=sorted(dict,key=lambda item:item[0])
print(dict(it))


