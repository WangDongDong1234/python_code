test_case_num = int(input().strip())
for i in range(test_case_num):
    line1 = [int(i) for i in input().strip().split()]
    line2 = [int(i) for i in input().strip().split()]
    k = line1[0]
    mid = sum(line2)/k
    # result = 0
    max_ = 0
    i=0
    part = 0
    while(i<len(line2)):
        part = part + line2[i]
        temp = part+line2[i]
        if(temp>mid):
            # print('----', part, temp)
            if mid-part < temp-mid:
                max_ = max(max_, part)
                i = i+1
            else:
                max_ = max(max_, temp)
                i = i+2
            part = 0
        else:
            i = i + 1

    print(max_)