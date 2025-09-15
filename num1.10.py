with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
result = ''

for i, current_letter in enumerate(text):
    result += current_letter

    if current_letter in vowels:

        prev = (i == 0) or (text[i-1] not in vowels)

        next = (i == len(text)-1) or (text[i+1] not in vowels)

        if prev and next:
            result += 'с' + current_letter.lower()
print(result)