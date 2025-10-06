# num1
# s = input().strip()
# parts = s.split('student_')[1:]
# students = []
# for part in parts:
#     number = part[:3]
#     score = int(part[3:])
#     students.append((number, score))
# max_score = max(students, key=lambda x: x[1])[1]
# result = []
# for number, score in students:
#     if score == max_score:
#         result.append(number)
# print('-'.join(result))


# num2
# import math
# r, a = map(float, input().split())
# length = 2 * math.pi * r
# s = math.pi * r * r
# square = a * a
# pr = s / square * 100
# print(f'Длина окружности равно {length:.2f}. Площадь круга составляет {pr:.2f}% от площади квадрата.')


# num3
# def func1(s1, s2):
#     first_part = s1[:2][::-1] + s1[2:]
#     second_part = s2[:2][::-1] + s2[2:]
#     return f'{first_part}-{second_part}'
#
# a, b = input().split()
# print(func1(a, b))


# num4
# def func3(s):
#     if len(s) < 4:
#         if all(c.isupper() for c in s):
#             return s.upper()
#         else:
#             return s
#     else:
#         up = sum(1 for c in s[:4] if c.isupper())
#         if up >= 3:
#             return s.upper()
#         else:
#             return s
#
# text = input()
# print(func3(text))


# num5
# def html(tag, text):
#     valid_tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
#     if tag in valid_tags:
#         return f'<{tag}>{text}</{tag}>'
#     else:
#         return 'Введён неверный тег'
#
# tag = input()
# text = input()
# print(html(tag, text))


# num6
# s = input()
# if len(s) <= 2:
#     print(ord(s[0]))
# elif len(s) < 10:
#     mid = len(s) // 2 - (1 if len(s) % 2 == 0 else 0)
#     print(ord(s[0]) + ord(s[mid]) + ord(s[-1]))
# else:
#     print(ord(s[-1]))
