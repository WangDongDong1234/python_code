n=int(input())

for i in range(n):
    totalKind_totalValue_str = input().strip()
    totalKind_totalValue = [int(item) for item in totalKind_totalValue_str.split(' ')]
    totalValue = totalKind_totalValue[1]
    kind_value_str = input().strip()
    kind_value = [int(item) for item in kind_value_str.split(' ')]
    kind_value.sort(reverse=True)
    sum = 0
    i = 0
    while totalValue > 0:
        if kind_value[i] <= totalValue:
            totalValue -= kind_value[i]
            sum += 1
        else:
            i += 1
        if i == len(kind_value):
            sum = -1
            break

    print(sum)