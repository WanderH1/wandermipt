# num1
# def find(data):
#     chunks = [chunk for chunk in data.split('student_') if chunk]
#
#     max_score = -1
#     best_students = []
#
#     for chunk in chunks:
#         student_id = chunk[:3]
#         score = int(chunk[3:])
#
#         if score > max_score:
#             max_score = score
#             best_students = [student_id]
#         elif score == max_score:
#             best_students.append(student_id)
#
#     return "-".join(best_students)
#
#
# input_data = input().strip()
# print(find(input_data))
# 
# num3
# def swap(s1, s2):
#     str1 = s1[:2][::-1] + s1[2:]
#     str2 = s2[:2][::-1] + s2[2:]
#
#     return f"{str1}-{str2}"
#
#
# word1, word2 = input().split()
# print(swap(word1, word2))

#num4
# def process_string(s):
#     if len(s) < 4:
#         if s.isupper():
#             return s.upper()
#         return s
#
#     upper_count = 0
#     for char in s[:4]:
#         if char.isupper():
#             upper_count += 1
#
#     if upper_count >= 3:
#         return s.upper()
#     else:
#         return s
#
#
# text = input()
# print(process_string(text))
#
# num5
# def wrap_in_tag(tag, text):
#     allowed_tags = ('a', 'abbr', 'b', 'body', 'caption', 'cite', 'code',
#                     'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
#                     'header', 'i', 's')
#
#     if tag in allowed_tags:
#         return f"<{tag}>{text}</{tag}>"
#     else:
#         return "Введён неверный тег"
#
#
# input_tag = input().strip()
# input_text = input().strip()
#
# print(wrap_in_tag(input_tag, input_text))
#
