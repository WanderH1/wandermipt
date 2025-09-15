t = input()
t=t.split(" ")
n = int(t[0])
a = t[1]
m = []
for i in range(0, len(a), int(len(a)/n)):
    m.append(a[i:i+int(len(a)/n)][::-1])
print(''.join(m))