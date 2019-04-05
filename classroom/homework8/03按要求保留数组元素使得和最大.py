n=int(input())

for i in range(n):
    num = int(input())
    array_str = input()
    array = [int(item) for item in array_str.split(' ')]
    array.sort(reverse=True)
    result = []
    length = len(array)
    while length:
        tmp = array.pop(0)
        length -= 1
        result.append(tmp)
        try:
            index = array.index(tmp - 1)
            array.remove(tmp - 1)
            length -= 1
        except ValueError:
            continue
    print(sum(result))