n=int(input())


for i in range(n):
    num = int(input())
    array_str = input().strip()
    array = [int(item) for item in array_str.split(' ')]
    max_num = max(array)
    array.remove(max_num)


    def dfs(start, sum):
        global max_num
        if start == num:
            if sum > max_num:
                max_num = sum
            return
        dfs(start + 1, sum)
        dfs(start + 1, sum + array[start - 1])


    dfs(1, max_num)
    print(max_num)