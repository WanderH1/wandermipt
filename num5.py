def func():
    b = input().split()
    n = b[0]
    u = int(b[1])
    v = int(b[2])
    k=0
    for i in n:
        k = k*u + int(i)
    if k == 0:
        return '0'
    digits =[]
    num = k
    while num > 0:
        num, remainder = divmod(num, v)
        digits.append(str(remainder))
    return ''.join(digits[::-1])
print(func())