first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
#Если все числа равны между собой, то вывести 3
if first == second and first == third and second == third:
    print(3)
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
elif first == second or first == third or second == third:
    print(2)
 #Если равных чисел среди 3-х вообще нет, то вывести 0
else:
    print(0)