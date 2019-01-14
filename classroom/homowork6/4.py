n=int(input())
last_result=[]
for i in range(n):
    str_s=input().strip()
    str_list=[item for item in str_s.split(",")]
    txt=str_list[0]
    part=str_list[1]
    result=[]
    book=True
    start=0
    while book:
        index=txt.find(part,start)
        if index!=-1:
            result.append(index)
            start=start+index+1
        else:
            book=False
    last_result.append(result)

for item in last_result:
    for w in range(len(item)):
        if w == 0:
            print(item[w], end="")
        else:
            print("",item[w],end="")
    print()