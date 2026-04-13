# num2
# import math
#
#
# def calculate_geometry():
#     r, a = map(float, input().split())
#     circumference = 2 * math.pi * r
#     circle_area = math.pi * (r ** 2)
#     square_area = a ** 2
#     percentage = (circle_area / square_area) * 100
#
#     print(f"Длина окружности равно"
#           f"{circumference:.2f}. Площадь круга составляет"
#           f"{percentage:.2f}% от площади квадрата.")
#
#
# if __name__ == '__main__':
#     calculate_geometry()
#
# num6
# def process_ascii(s):
#     n = len(s)
#     if n <= 2:
#         return ord(s[0])
#     elif n <= 10:
#         mid_idx = (n - 1) // 2
#         return ord(s[0]) + ord(s[mid_idx]) + ord(s[-1])
#     else:
#         return ord(s[-1])
# 
# 
# text = input()
# print(process_ascii(text))
# 

