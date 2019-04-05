"""
  该题关键在于如何划分各L型骨牌所在位置区域。我们发现，L型骨牌占三个方格，我们可以把棋盘从中央分为四块，那么这四块子棋盘中仅一块是有特殊方格的，可以用一块骨牌使得其他三块子棋盘均被覆盖。以此为原则，无论这种分法是否最终可解，我们首先保证了每个子棋盘都有一个特殊方格，所以，分治的模型就出来了。

"""
n=int(input())

for m in range(n):
    start_special_str = input().strip()
    start_special = [int(item) for item in start_special_str.split(' ')]
    # 开始的标号
    start = start_special[0]
    # 特殊点的坐标
    special_x = start_special[1]
    special_y = start_special[2]
    # 查找点的坐标
    location_str = input().strip()
    location = [int(item) for item in location_str.split(' ')]
    location_x = location[0]
    location_y = location[1]

    array = []
    for i in range(32):
        tmp = []
        for j in range(32):
            tmp.append('a')
        array.append(tmp)
    array[special_x][special_y] = 0


    def divide(zx, zy, si, x, y):
        if si == 1:
            return
        mid = int(si / 2)
        mid_x = zx + mid - 1
        mid_y = zy + mid - 1
        global start
        # 在左上

        if x <= mid_x and y <= mid_y:
            array[mid_x + 1][mid_y + 1] = start
            array[mid_x + 1][mid_y] = start
            array[mid_x][mid_y + 1] = start
            start += 1
            # 左上
            divide(zx, zy, mid, x, y)
            # 右上
            divide(zx, zy + mid, mid, zx + mid - 1, zy + mid)
            # 左下
            divide(zx + mid, zy, mid, zx + mid, zy + mid - 1)
            # 右下
            divide(zx + mid, zy + mid, mid, zx + mid, zy + mid)
        # 在右上
        if x <= mid_x and y > mid_y:
            array[mid_x + 1][mid_y + 1] = start
            array[mid_x][mid_y] = start
            array[mid_x + 1][mid_y] = start
            start += 1
            # 左上
            divide(zx, zy, mid, mid_x + mid - 1, mid_y + mid - 1)
            # 右上
            divide(zx, zy + mid, mid, x, y)
            # 左下
            divide(zx + mid, zy, mid, zx + mid, zy + mid - 1)
            # 右下
            divide(zx + mid, zy + mid, mid, zx + mid, zy + mid)

        # 左下
        if x > mid_x and y <= mid_y:
            array[mid_x][mid_y] = start
            array[mid_x][mid_y + 1] = start
            array[mid_x + 1][mid_y + 1] = start
            start += 1
            # 左上
            divide(zx, zy, mid, zx + mid - 1, zy + mid - 1)
            # 右上
            divide(zx, zy + mid, mid, zx + mid - 1, zy + mid)
            # 左下
            divide(zx + mid, zy, mid, x, y)
            # 右下
            divide(zx + mid, zy + mid, mid, zx + mid, zy + mid)
        # 右下
        if x > mid_x and y > mid_y:
            array[mid_x][mid_y] = start
            array[mid_x][mid_y + 1] = start
            array[mid_x + 1][mid_y] = start

            start += 1
            # 左上
            divide(zx, zy, mid, zx + mid - 1, zy + mid - 1)
            # 右上
            divide(zx, zy + mid, mid, zx + mid - 1, zy + mid)
            # 左下
            divide(zx + mid, zy, mid, zx + mid - 1, zy + mid - 1)
            # 右下
            divide(zx + mid, zy + mid, mid, x, y)


    divide(0, 0, 32, special_x, special_y)

    next = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    sum = 1
    for item in next:
        next_x = location_x + item[0]
        next_y = location_y + item[1]
        if array[next_x][next_y] == array[location_x][location_y]:
            if sum == 1:
                print(next_x, next_y, end=',')
                sum += 1
            else:
                print(next_x, next_y)
