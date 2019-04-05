str_str=input().strip()
str=[int(item) for item in str_str.split(' ')]
start=str[0]
end=str[1]
k=str[2]
sum=0
if k-1>=2:
    for i in range(start,end+1):
        if i%k==0:
            for j in range(2,k):
                if i%j!=0:
                    sum+=1
                else:
                    break
else:
    for i in range(start,end+1):
        if i%k==0:
            for j in range(2,i):
                if i%j!=0:
                    sum+=1
                else:
                    break

print(sum)