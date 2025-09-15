n = int(input())
a = list(map(int, input().split()))

for num in a:
    count_less = 0
    count_more = 0
    for other in a:
        if other < num:
            count_less += 1
        elif other > num:
            count_more += 1

    if count_less == count_more:
        print(num)
        break