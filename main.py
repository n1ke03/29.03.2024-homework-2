# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня неде-
# ли. Например, если 1, то на экране надпись понедельник,
# 2 - вторник и т.д.

# week = int(input("Введите номер дня недели: "))
# if week == 1:
#   print("Понедельник")
# elif week == 2:
#   print("Вторник")
# elif week == 3:
#   print("Среда")
# elif week == 4:
#   print("Четверг")
# elif week == 5:
#   print("Пятница")
# elif week == 6:
#   print("Суббота")
# elif week == 7:
#   print("Воскресенье")
# else:
#   print("Неверный номер дня недели")


# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2—фев-
# раль и т.д.

# month = int(input("Введите номер месяца: "))
# if month == 1:
#   print("Январь")
# elif month == 2:
#   print("Февраль")
# elif month == 3:
#   print("Март")
# elif month == 4:
#   print("Апрель")
# elif month == 5:
#   print("Май")
# elif month == 6:
#   print("Июнь")
# elif month == 7:
#   print("Июль")
# elif month == 8:
#   print("Август")
# elif month == 9:
#   print("Сентябрь")
# elif month == 10:
#   print("Октябрь")
# elif month == 11:
#   print("Ноябрь")
# elif month == 12:
#   print("Декабрь")    
# else:
#   print("Неверный номер месяца")


# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

number = int(input("Введите целое число: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is equal to zero")
else:
    print("Неверный ввод")


# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.