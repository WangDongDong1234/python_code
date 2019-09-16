n=int(input())
s=set()
for i in range(n):
    tmp=int(input())
    s.add(tmp)
l=list(s)
l.sort()
for e in l:
    print(e)