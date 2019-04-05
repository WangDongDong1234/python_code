str=input().strip()
n=int(input())
if n>len(str):
    print(-1)
else:
    for i in range(n,len(str)):
        print(str[i-n:i],end=" ")