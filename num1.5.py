a = list(map(int, input().split()))
n = int(input())
res = a[-n:] + a[:-n]
print(res)