#归并排序的非递归实现
def merge(seq,low,mid,height):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 通过low,mid height 将[low:mid) [mid:height)提取出来
    left = seq[low:mid]
    right = seq[mid:height]
    # print('left:', left, 'right:', right)

    k = 0   #left的下标
    j = 0   #right的下标
    result = [] #保存本次排序好的内容
    #将最小的元素依次添加到result数组中
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    #将对比完后剩余的数组内容 添加到已排序好数组中
    result += left[k:]
    result += right[j:]
    #将原始数组中[low:height)区间 替换为已经排序好的数组
    seq[low:height] = result
    # print("seq:", seq)

#seq = [5, 4, 3, 0, 1, 2, 7, 5, 11,9]

while 1:
    try:
        str=input().strip()
        list=[int(item) for item in str.split(" ")]
        n=list[0]
        seq=list[1::]
        i = 1
        while i < len(seq):
            # print('子数组 长度 : ', i)
            low = 0
            while low < len(seq):
                mid = low + i
                height = min(low + 2 * i, len(seq))
                if mid < height:
                    # print('low ', low, 'mid:', mid, 'height:', height)
                    merge(seq, low, mid, height)
                low += 2 * i
            i *= 2

        print(seq[0], end='')
        for i in range(1, n):
            print('', seq[i], end='')
        print()
    except EOFError:
        break


