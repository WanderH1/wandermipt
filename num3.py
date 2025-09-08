a = list(map(int, input().split()))
m=0
for i in range(len(a)):
    m+=a[i]
print(m/len(a))