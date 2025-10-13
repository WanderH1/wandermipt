# num3
#
# gravitational_constant = 6.67408E-11
# """Гравитационная постоянная Ньютона G"""
#
#
# class Star():
#     """Тип данных, описывающий звезду.
#     Содержит массу, координаты, скорость звезды,
#     а также визуальный радиус звезды в пикселах и её цвет.
#     """
#
#     type = "star"
#     """Признак объекта звезды"""
#
#     m = 0
#     """Масса звезды"""
#
#     x = 0
#     """Координата по оси **x**"""
#
#     y = 0
#     """Координата по оси **y**"""
#
#     Vx = 0
#     """Скорость по оси **x**"""
#
#     Vy = 0
#     """Скорость по оси **y**"""
#
#     Fx = 0
#     """Сила по оси **x**"""
#
#     Fy = 0
#     """Сила по оси **y**"""
#
#     R = 5
#     """Радиус звезды"""
#
#     color = "red"
#     """Цвет звезды"""
#
#     image = None
#     """Изображение звезды"""
#
#
# class Planet():
#     """Тип данных, описывающий планету.
#     Содержит массу, координаты, скорость планеты,
#     а также визуальный радиус планеты в пикселах и её цвет
#     """
#
#     type = "planet"
#     """Признак объекта планеты"""
#
#     m = 0
#     """Масса планеты"""
#
#     x = 0
#     """Координата по оси **x**"""
#
#     y = 0
#     """Координата по оси **y**"""
#
#     Vx = 0
#     """Скорость по оси **x**"""
#
#     Vy = 0
#     """Скорость по оси **y**"""
#
#     Fx = 0
#     """Сила по оси **x**"""
#
#     Fy = 0
#     """Сила по оси **y**"""
#
#     R = 5
#     """Радиус планеты"""
#
#     color = "green"
#     """Цвет планеты"""
#
#     image = None
#     """Изображение планеты"""
#
#
# def calculate_force(body, space_objects):
#     """Вычисляет силу, действующую на тело.
#
#     Параметры:
#
#     **body** — тело, для которого нужно вычислить дейстующую силу.
#
#     **space_objects** — список объектов, которые воздействуют на тело.
#     """
#
#     body.Fx = body.Fy = 0
#
#     for obj in space_objects:
#         if body != obj:
#             dx = obj.x - body.x
#             dy = obj.y - body.y
#             r = (dx ** 2 + dy ** 2) ** 0.5
#             F = gravitational_constant * body.m * obj.m / r ** 2
#             body.Fx += F * dx / r
#             body.Fy += F * dy / r
#         else:
#             continue
#
# def move_space_object(body, dt):
#     """Перемещает тело в соответствии с действующей на него силой.
#
#     Параметры:
#
#     **body** — тело, которое нужно переместить.
#     """
#
#     ax = body.Fx/body.m
#     body.Vx += ax * dt
#     body.x += body.Vx*dt
#     ay = body.Fy/body.m
#     body.Vy += ay * dt
#     body.y += body.Vy*dt
#
#
#
# def recalculate_space_objects_positions(space_objects, dt):
#     """Пересчитывает координаты объектов.
#
#     Параметры:
#
#     **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
#
#     **dt** — шаг по времени
#     """
#
#     for body in space_objects:
#         calculate_force(body, space_objects)
#     for body in space_objects:
#         move_space_object(body, dt)
#     central_body = None
#     max_mass = 0
#     for obj in space_objects:
#         if obj.m > max_mass:
#             max_mass = obj.m
#             central_body = obj
#
#     for body in space_objects:
#         if body.type == "planet" and central_body and body != central_body:
#             rx = body.x - central_body.x
#             ry = body.y - central_body.y
#             r = (rx ** 2 + ry ** 2) ** 0.5
#
#             vx = body.Vx - central_body.Vx
#             vy = body.Vy - central_body.Vy
#
#             if r > 0:
#                 tangential_velocity = abs(rx * vy - ry * vx) / r
#                 body.angular_velocity = tangential_velocity / r
#                 body.sectorial_velocity = 0.5 * r * tangential_velocity
#
# if __name__ == "__main__":
#     print("This module is not for direct call!")



# num2
# from random import randrange as rnd, choice
# from tkinter import *
# import math
#
# import time
#
# root = Tk()
# fr = Frame(root)
# root.geometry('800x600')
# canv = Canvas(root, bg='white')
# canv.pack(fill=BOTH, expand=1)
#
#
# class Ball():
#     """ Класс Ball описывает мяч. """
#
#     def __init__(self, x=40, y=450):
#         """ Конструктор класса Ball
#         Args:
#         x - начальное положение мяча по горизонтали
#         y - начальное положение мяча по вертикали
#         """
#         self.x = x
#         self.y = y
#         self.r = 10
#         self.vx = 0
#         self.vy = 0
#         self.color = choice(['blue', 'green', 'red', 'brown'])
#         self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
#         self.live = 30
#
#     def set_coords(self):
#         canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
#
#     def move(self):
#         """ Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
#         self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
#             и стен по краям окна (размер окна 800х600).
#         """
#         # TODO
#         self.x += self.vx
#         self.y -= self.vy
#         self.vy-= 1
#
#         if self.x + self.r > 800 or self.x - self.r < 0:
#             self.vx = -self.vx * 0.8
#         if self.y + self.r > 600:
#             self.vy = -self.vy * 0.8
#             self.y = 600 - self.r
#         if self.y - self.r < 0:
#             self.vy = -self.vy * 0.8
#
#         self.set_coords()
#         self.live -= 1
#
#     def hittest(self, ob):
#         """ Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте ob.
#
#         Args:
#             ob: Обьект, с которым проверяется столкновение.
#         Returns:
#             Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
#         """
#         # TODO
#         distance = math.sqrt((self.x - ob.x) ** 2 + (self.y - ob.y) ** 2)
#         return distance <= self.r + ob.r
#
#
# class gun():
#     """ Класс gun описывает пушку. """
#
#     def __init__(self, x=40, y=450):
#         self.f2_power = 10
#         self.f2_on = 0
#         self.an = 1
#         self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...
#
#     def fire2_start(self, event):
#         self.f2_on = 1
#
#     def fire2_end(self, event):
#         """ Выстрел мячом происходит при отпускании кнопки мыши.
#         Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
#         """
#         global balls, bullet
#         bullet += 1
#         new_ball = Ball()
#         new_ball.r += 5
#         self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
#         new_ball.vx = self.f2_power * math.cos(self.an)
#         new_ball.vy = -self.f2_power * math.sin(self.an)
#         balls += [new_ball]
#         self.f2_on = 0
#         self.f2_power = 10
#
#     def targetting(self, event=0):
#         """ Прицеливание. Зависит от положения мыши.
#         """
#         if event:
#             self.an = math.atan((event.y - 450) / (event.x - 20))
#         if self.f2_on:
#             canv.itemconfig(self.id, fill='orange')
#         else:
#             canv.itemconfig(self.id, fill='black')
#         canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
#                     450 + max(self.f2_power, 20) * math.sin(self.an))
#
#     def power_up(self):
#         if self.f2_on:
#             if self.f2_power < 100:
#                 self.f2_power += 1
#             canv.itemconfig(self.id, fill='orange')
#         else:
#             canv.itemconfig(self.id, fill='black')
#
#
# class target():
#     """ Класс target описывает цель. """
#
#     def __init__(self, x=40, y=450):
#         self.points = 0
#         self.live = 1
#         # TODO: don't work!!! How to call this functions when object is created?
#         self.id = canv.create_oval(0,0,0,0)
#         self.id_points = canv.create_text(30,30,text = self.points,font = '28')
#         self.new_target()
#
#     def new_target(self):
#         """ Инициализация новой цели. """
#         x = self.x = rnd(600, 780)
#         y = self.y = rnd(300, 550)
#         r = self.r = rnd(2, 50)
#         color = self.color = 'red'
#         canv.coords(self.id, x - r, y - r, x + r, y + r)
#         canv.itemconfig(self.id, fill=color)
#
#     def hit(self, points=1):
#         """ Попадание шарика в цель. """
#         canv.coords(self.id, -10, -10, -10, -10)
#         self.points += points
#         canv.itemconfig(self.id_points, text=self.points)
#
#
# t1 = target()
# screen1 = canv.create_text(400, 300, text='', font='28')
# g1 = gun()
# bullet = 0
# balls = []
#
#
# def new_game(event=''):
#     global gun, t1, screen1, balls, bullet
#     t1.new_target()
#     bullet = 0
#     balls = []
#     canv.bind('<Button-1>', g1.fire2_start)
#     canv.bind('<ButtonRelease-1>', g1.fire2_end)
#     canv.bind('<Motion>', g1.targetting)
#
#     z = 0.03
#     t1.live = 1
#     while t1.live or balls:
#         for b in balls:
#             b.move()
#             if b.hittest(t1) and t1.live:
#                 t1.live = 0
#                 t1.hit()
#                 canv.bind('<Button-1>', '')
#                 canv.bind('<ButtonRelease-1>', '')
#                 canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
#         canv.update()
#         time.sleep(0.03)
#         g1.targetting()
#         g1.power_up()
#     canv.itemconfig(screen1, text='')
#     canv.delete(gun)
#     root.after(750, new_game)
#
#
# new_game()
#
# rt.mainloop()

# num1
# class Vector:
#     def __init__(self, coords):
#         coords = coords.strip('{}')
#         parts = coords.split(',')
#         self.x = float(parts[0].strip())
#         self.y = float(parts[1].strip())
#         self.z = float(parts[2].strip())
#         assert all(isinstance(i, (int, float)) for i in [self.x, self.y, self.z])
#
#     def __abs__(self):
#         return (self.x**2 + self.y**2 + self.z**2)**0.5
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(f"{{{self.x + other.x}, {self.y + other.y}, {self.z + other.z}}}")
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(f"{{{self.x - other.x}, {self.y - other.y}, {self.z - other.z}}}")
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         elif isinstance(other, (int, float)):
#             return Vector(f"{{{self.x * other}, {self.y * other}, {self.z * other}}}")
#         return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def cross(self, other):
#         return Vector(f"{{{self.y * other.z - self.z * other.y}, "
#                       f"{self.z * other.x - self.x * other.z}, "
#                       f"{self.x * other.y - self.y * other.x}}}")
#
#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#
# def triangle(a, b, c):
#     ab = b - a
#     ac = c - a
#     cross_product = ab.cross(ac)
#     return 0.5 * abs(cross_product)
#
# a = Vector("{1, 2, 3}")
# b = Vector("{4, 5, 6}")
# vectors = [
#     Vector("{1, 1, 1}"),
#     Vector("{2, 3, 2}"),
#     Vector("{4, 3, 1}"),
#     Vector("{4, 5, 6}"),
#     Vector("{0, 0, 0}"),
#     Vector("{5, 2, 4}")
# ]
#
# n = len(vectors)
# res_vector = Vector("{0, 0, 0}")
#
# for v in vectors:
#     res_vector = res_vector + v
#
# cm = res_vector * (1/n)
#
# max_area = 0
# best_triangle = None
#
# for i in range(len(vectors)):
#     for j in range(i + 1, len(vectors)):
#         for k in range(j + 1, len(vectors)):
#             area = triangle(vectors[i], vectors[j], vectors[k])
#             if area > max_area:
#                 max_area = area
#                 best_triangle = (vectors[i], vectors[j], vectors[k])
#
# print(f"Центр масс: {cm}")
# print(f"Модуль вектора a: {abs(a)}")
# print(f"Модуль вектора b: {abs(b)}")
# print(f"Скалярное произведение a*b: {a * b}")
# print(f"Треугольник с максимальной площадью: {best_triangle[0]}, {best_triangle[1]}, {best_triangle[2]}")
# print(f"Максимальная площадь: {max_area:.2f}")
