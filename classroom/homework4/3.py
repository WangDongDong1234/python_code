n=int(input())
result=[]
for i in range(0,n):
    huajia_muban = input().strip()
    huajia = huajia_muban.split(" ")[0]
    muban = huajia_muban.split(" ")[1]
    str_muban=input()
    lst_muban=[]
    tmp_muban=str_muban.strip().split(" ")
    for item in tmp_muban:
        lst_muban.append(int(item))
    if huajia>=muban:
        result.append(max(lst_muban))
        continue
    else:
        for t in range(0,huajia):



