a = input().split()
m = 0
for i in range(len(a)):
    if a.count(a[i]) > m:
        m = int(a[i])
print(m)