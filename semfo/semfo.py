# num1
# import matplotlib.pyplot as plt
# x_eval = [0.1928, 0.2003, 0.2275, 0.2516, 0.2816, 0.3007, 0.3257, 0.3485, 0.3741, 0.4043, 0.425, 0.4483, 0.4745, 0.497]
# y_eval = [0.55, 0.6, 0.65, 0.75, 0.85, 0.9, 1, 1.05, 1.15, 1.25, 1.3, 1.35, 1.45, 1.5]
# plt.figure()
# plt.title('Измерение удельного сопротивления нихромовой проволоки')
# plt.xlabel('Напряжение U, В')
# plt.ylabel('Сила тока I, А')
# plt.grid(True)
# plt.plot(x_eval, y_eval)
# plt.show()

#num2
# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure(figsize = (16,9), dpi = 100)
# ax1 = fig.add_subplot(311)
# ax2 = fig.add_subplot(312)
# ax3 = fig.add_subplot(313)
# values1 = np.random.normal(0, 10, 1000)
# values2 = np.random.normal(0, 10, 1000)
# values3 = np.random.normal(0, 10, 1000)
# ax1.hist(values1, bins = 50)
# ax1.grid()
# ax2.hist(values2, bins = 50)
# ax2.grid()
# ax3.hist(values3, bins = 50)
# ax3.grid()
# x = [i for i in range(50)]
# y = [j**1.5 for j in x]
# plt.show()


# num3
# import matplotlib.pyplot as plt
#
# file = open('iris_data.csv', 'r')
# a=[]
# b=[]
# lines = file.readlines()
# for line in lines[1:]:
#     line=line.split(',')
#     a.append(line[-1][5:-1])
#     if float(line[3]) <= 1.2:
#         b.append(1.2)
#     elif 1.2 <= float(line[3]) <= 1.5:
#         b.append(1.3)
#     elif float(line[3]) >= 1.5:
#         b.append(1.5)
# s=set(a)
# fig = plt.figure(figsize=(16,9))
# ax1 = fig.add_subplot(211)
# ax1.set_title('Разновидности')
# plt.pie([a.count(i) for i in s], labels = s)
# ax2 = fig.add_subplot(212)
# ax2.set_title('Длины')
# plt.pie([b.count(1.2),b.count(1.3),b.count(1.5)], labels = ['До 1.2','От 1.2 до 1.5','От 1.5'])
# plt.show()


# num4
# import matplotlib.pyplot as plt
# import numpy as np
#
# file = open('iris_data.csv', 'r')
# lines = file.readlines()
#
# sepal_length = []
# sepal_width = []
# petal_length = []
# petal_width = []
# species = []
#
# for line in lines[1:]:
#     parts = line.strip().split(',')
#     sepal_length.append(float(parts[1]))
#     sepal_width.append(float(parts[2]))
#     petal_length.append(float(parts[3]))
#     petal_width.append(float(parts[4]))
#     species.append(parts[5])
#
# file.close()
#
# fig, axes = plt.subplots(2, 3, figsize=(15, 10))
#
# combinations = [
#     (sepal_length, sepal_width, 'SepalLengthCm', 'SepalWidthCm'),
#     (sepal_length, petal_length, 'SepalLengthCm', 'PetalLengthCm'),
#     (sepal_length, petal_width, 'SepalLengthCm', 'PetalWidthCm'),
#     (sepal_width, petal_length, 'SepalWidthCm', 'PetalLengthCm'),
#     (sepal_width, petal_width, 'SepalWidthCm', 'PetalWidthCm'),
#     (petal_length, petal_width, 'PetalLengthCm', 'PetalWidthCm')
# ]
#
# for i, (x_data, y_data, x_label, y_label) in enumerate(combinations):
#     ax = axes[i // 3, i % 3]
#     ax.scatter(x_data, y_data, alpha=0.7)
#     ax.set_xlabel(x_label)
#     ax.set_ylabel(y_label)
#     ax.set_title(f'{x_label} vs {y_label}')
#
#     if len(x_data) > 1:
#         coefficients = np.polyfit(x_data, y_data, 1)
#         polynomial = np.poly1d(coefficients)
#         x_fit = np.linspace(min(x_data), max(x_data), 100)
#         y_fit = polynomial(x_fit)
#         ax.plot(x_fit, y_fit, color='red', linewidth=2)
#
#         equation = f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}'
#         ax.text(0.05, 0.95, equation, transform=ax.transAxes,
#                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
#                 verticalalignment='top')
#
#         print(f'{y_label} от {x_label}: {equation}')
#
# plt.tight_layout()
# plt.show()


# num5
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# df = pd.read_csv('BTC_data.csv')
# dates = []
# prices = []
#
# for index, row in df.iterrows():
#     date_str = row.iloc[0]
#     date_obj = datetime.strptime(date_str.split('T')[0], '%Y-%m-%d')
#     formatted_date = date_obj.strftime('%d-%m-%y')
#
#     dates.append(formatted_date)
#     close_price = row.iloc[-1]
#     prices.append(close_price)
# plt.figure(figsize=(12, 6))
# plt.plot(dates, prices, linewidth=1.5, color='blue')
#
# plt.title('Исторический график цены биткоина', fontsize=14)
# plt.xlabel('Дата (DD-MM-YY)', fontsize=12)
# plt.ylabel('Цена закрытия (USD)', fontsize=12)
# plt.grid(True, alpha=0.3)
# n = max(1, len(dates) // 10)
# plt.xticks(range(0, len(dates), n), rotation=45)
#
# plt.tight_layout()
# plt.show()


# num6
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# df = pd.read_csv('BTC_data.csv')
#
# dates = []
# prices = []
#
# for index, row in df.iterrows():
#     date_str = row.iloc[0]
#     date_obj = datetime.strptime(date_str.split('T')[0], '%Y-%m-%d')
#     formatted_date = date_obj.strftime('%d-%m-%y')
#     dates.append(formatted_date)
#     close_price = row.iloc[-1]
#     prices.append(close_price)
#
# x = np.arange(len(prices))
# y = np.array(prices)
#
# coefficients = np.polyfit(x, y, 3)
# polynomial = np.poly1d(coefficients)
#
# poly_values = polynomial(x)
#
# plt.figure(figsize=(12, 6))
#
# plt.plot(dates, prices, linewidth=2, color='blue', label='Фактическая цена')
#
# plt.plot(dates, poly_values, linewidth=2, color='red', linestyle='--', label='Аппроксимация полиномом 3-й степени')
#
# plt.title('Аппроксимация цены биткоина полиномом 3-й степени', fontsize=14)
# plt.xlabel('Дата (DD-MM-YY)', fontsize=12)
# plt.ylabel('Цена закрытия (USD)', fontsize=12)
# plt.grid(True, alpha=0.3)
# plt.legend()
#
# n = max(1, len(dates) // 10)
# plt.xticks(range(0, len(dates), n), rotation=45)
#
# plt.tight_layout()
# plt.show()
#
# print("Коэффициенты полинома 3-й степени:")
# print(coefficients)
# print("\nПолиномиальная функция:")
# print(polynomial)
