with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
count = 0
i = 0
n = len(text)

while i < n:
    if text[i] in '.!?':
        count += 1
        i += 1
        while i < n and text[i] in '.!?':
            i += 1
    else:
        i += 1
print(count)