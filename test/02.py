s=input().strip()
new_s=s.lower()
#print(new_s)
dict={}
for i in range(len(new_s)):
    if dict.get(new_s[i])==None:
        dict[new_s[i]]=[i]
    else:
        dict[new_s[i]].append(i)
keys=[]
for key,value in dict.items():
    if len(value)<=1:
        keys.append(key)
for item in keys:
    del dict[item]

book=[]
for i in range(len(new_s)):
    book.append(0)
for key,value in dict.items():
    for item in value:
        book[item]=key
del_keys=[]
for i in range(len(new_s)):
    if book[i]!=0:
        if new_s[i]>new_s[i+1]:
            del_keys.append(i)
        else:
            for j in range(i+1,len(new_s)):
                if book[j]==book[i]:
                    del_keys.append(j)
del_keys.sort(reverse=True)
str_lsit=[]
for item in new_s:
    str_lsit.append(item)
for item in del_keys:
    del str_lsit[item]
print(str_lsit[0])




