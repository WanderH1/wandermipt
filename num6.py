with open("input.txt") as f:
    nums, op, base = f.read().splitlines()

nums = nums.split()
base = int(base)

dec_nums = [int(num, base) for num in nums]

if op == '+':
    res = sum(dec_nums)
elif op == '-':
    res = dec_nums[0] - sum(dec_nums[1:])
elif op == '*':
    res = 1
    for num in dec_nums:
        res *= num

result = ""
n = abs(res)
while n:
    n, digit = divmod(n, base)
    result = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[digit] + result

result = result or "0"
if res < 0:
    result = "-" + result

with open("output.txt", "w") as f:
    f.write(result)