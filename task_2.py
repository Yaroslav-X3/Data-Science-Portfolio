print("Виконав студент групи КМ-12 Якімов Ярослав\n")
print("Лабораторна робота №1\n")
print("Тема. Програмування лінійних алгоритмів та розгалужених процесів\n")
print("Завдання №2. Обчислення в математичних задачах\n")
print("29) Два прямокутники, розташовані в першому квадраті, зі сторонами, паралельними")
print("осям координат, задано координатами своїх лівого верхнього і правого нижнього")
print("кутів. Для першого прямокутника це точки (x1, y1) і (х2, 0), для другого -")
print("(x3, y3), (х4, 0). Скласти програму, що визначає, чи перетинаються дані")
print("прямокутники, і обчислює площу загальної частини, якщо вона існує. Всі величини")
print("вводити з клавіатури.\n")

x1 = y1 = x2 = x3 = y3 = x4 = ""

print("Введіть значення x1:")
while not x1.isnumeric(): x1 = input()

x1 = int(x1)

print("Введіть значення y1:")
while not y1.isnumeric(): y1 = input()

y1 = int(y1)

print("Введіть значення x2:")
while not x2.isnumeric(): x2 = input()

x2 = int(x2)

print("Введіть значення x3:")
while not x3.isnumeric(): x3 = input()

x3 = int(x3)

print("Введіть значення y3:")
while not y3.isnumeric(): y3 = input()

y3 = int(y3)

print("Введіть значення x4:")
while not x4.isnumeric(): x4 = input()

x4 = int(x4)

if x3>=x1 and x2>=x3:
    intrL = x3
elif x1>=x3 and x4>=x1:
    intrL = x1
else: intrL = None
    
if x2>=x3 and x4>=x2:
    intrR = x2
elif x4>=x1 and x2>=x4:
    intrR = x4
else: intrR = None

if y1>=y3:
    medY = y3
else: medY = y1

if(intrL == None or intrR == None):
    print("Прямокутники не перетинаються.")
else:
    print("Прямокутники перетинаються.")
    print("Площа перетину: "+str((int(intrR)-int(intrL))*int(medY)))
    
