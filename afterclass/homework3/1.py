str1=input()
str2=input()
same_str=[]
for item in str1:
    if item in str2:
        same_str.append(item)
# print(same_str)
sam_str=""
for item in same_str:
    sam_str+=item
# print(sam_str)
tmp_str1=""
tmp_str2=""
for item in str1:
    if item in sam_str:
        tmp_str1+=item
for item in str2:
    if item in sam_str:
        tmp_str2+=item
print(tmp_str1)
print(tmp_str2)





