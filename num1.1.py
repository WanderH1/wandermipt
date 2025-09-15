a=input()
b=a[2:].replace(" ", "")
for i in range(1, int(a[0])+1):
    if b.find(f'{i}')==-1:
        print(i)