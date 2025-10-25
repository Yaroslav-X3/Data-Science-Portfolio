import math

print("Виконав студент групи КМ-12 Якімов Ярослав\n")
print("Лабораторна робота №1\n")
print("Тема. Програмування лінійних алгоритмів та розгалужених процесів\n")
print("Завдання №3. Обчислення конкретної функції, в залежності від введеного значення х\n")
print("29)\nF(x) = ")
print(" --- sin(x) + x^2, якщо x < 0")
print(" --- cos(x) + sin(x), якщо 0 <= x < π/2")
print(" --- x - cos(x), якщо x > π/2\n")

print("Введіть значення x:")

x = ""

while not x.isnumeric() and (not len(x.split('.')) == 2 or not x.split('.')[0].isnumeric() or not x.split('.')[1].isnumeric()): x = input()

x = float(x)

if(x<0): print("Відповідь: "+str(math.sin(x)+x**2))
if(x>=0 and x <= math.pi/2): print("Відповідь: "+str(math.cos(x) + math.sin(x)))
if(x>math.pi/2): print("Відповідь: "+str(x - math.cos(x)))
