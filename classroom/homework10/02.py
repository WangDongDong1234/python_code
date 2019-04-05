n=int(input())

for i in range(n):
    nums = int(input())
    start_str = input().strip()
    # print(start_str.split(' '))
    start = [int(item) for item in start_str.split(' ')]
    end_str = input().strip()
    end = [int(item) for item in end_str.split(' ')]
    array = []
    for i in range(nums):
        tmp = []
        tmp.append(start[i])
        tmp.append(end[i])
        array.append(tmp)
    array.sort(key=lambda item: item[1])
    # print(array)
    sum = 1
    tmp_time = array[0][1]
    for i in range(1, len(array)):
        if array[i][0] > tmp_time:
            tmp_time = array[i][1]
            sum += 1
    print(sum)
