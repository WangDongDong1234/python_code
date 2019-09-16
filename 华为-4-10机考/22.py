str=input().strip()
tmp_str=str[::-1]
while str.find("(")!=-1:
    #右括号
    j=str.find(")")
    #做括号
    i=len(str)-1-tmp_str.find("(")

    n=int(str[i-1])
    t=str[i+1:j]
    tmp=""
    for ik in range(n):
        tmp+=t
    str = str[:i - 1] + tmp + str[j + 1:]
    tmp_str = str[::-1]



print(str[::-1])

