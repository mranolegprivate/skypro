
### **Задание 1. Настройте рабочее окружение**

1. Установите на свой компьютер Python.
2. Установите Visual Studio Code.
3. В VS Code установите плагин python.

Видеоинструкцию по трем шагам вы найдете в видео первого урока.

### **[Задание 2](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_1.py "Задание 2"). Создайте переменную**

1. Создайте файл lesson_1_task_1.py.
2. Откройте его в VS Code.
3. В файле создайте переменную my_name.
4. Присвойте переменной значение — ваше имя. Помните, что строковые значения указываются в кавычках.
5. Напишите команду вывода значения переменной на экран. Используйте функцию `print`.
6. В правом верхнем углу нажмите кнопку play. В консоль выведется значение переменной.

Убедитесь, что в VS Code включено автосохранение («Файл» -> «Автосохранение»).
```
my_name = "Олег"

print(my_name)
```
### **[Задание 3](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_2.py "Задание 3"). Перезапишите переменную**

1. Создайте файл lesson_1_task_2.py.
2. В файле создайте переменную my_age и присвойте ей значение — ваш возраст.
3. В следующей строке присвойте этой же переменной другое значение — ваш возраст через 3 года.
4. Напишите команду вывода значения переменной на экран. Используйте функцию `print`.
5. Запустите скрипт.

```
my_age = 35
my_age =38
print(my_age)
```

### **[Задание 4](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_3.py "Задание 4"). Получите пользовательский ввод**

1. Создайте файл lesson_1_task_3.py.
2. Создайте переменную user_name.
3. Значением переменной будет результат ввода от пользователя. 

Используйте функцию input().
Пример: user_name = input("Ваше имя:"). 

1. Далее напишите команду вывода user_name на экран в формате «Привет, user_name».

Строки можно складывать.
Пример: "abc"+"123" = "abc123"
```
user_name = input()

print(user_name)

print("Привет, " + user_name)
```
### **[Задание 5](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_4.py "Задание 5"). Получите пользовательский ввод**

1. Создайте файл lesson_1_task_4.py.
2. Создайте переменную first_name.
3. Создайте переменную last_name.
4. Задайте значение обеих переменных через функцию input.
5. Выведите на экран текст в формате «Вас зовут: last_name first_name».
```
first_name = input("Введите Ваше имя: ")
last_name = input("Введите Вашу фамилию: ")

print("Вас зовут:", last_name, first_name)
```
### **[Задание 6](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_6.py "Задание 6"). Создание функции**

1. Создайте файл lesson_1_task_6.py.
2. Объявите функцию print_greeting().
3. Тело функции: печать на экран выражения «Привет, мир!».
4. Напишите код, который вызывает функцию print_greeting().

Объявление функции (def) должно быть в коде **до** ее вызова.
```
def print_greeting():
    print("Привет, Мир!")

print_greeting()
```
### **[Задание 7](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_7.py "Задание 7"). Вызов функций**

1. Создайте файл lesson_1_task_7.py
2. Создайте по одной функции на каждое действие (всего 10 функций):
    1. Вывести в консоль 1
    2. Вывести в консоль 2
    3. Вывести в консоль 3
    4. Вывести в консоль 4
    5. Вывести в консоль 5
    6. Вывести в консоль 6
    7. Вывести в консоль 7
    8. Вывести в консоль 8
    9. Вывести в консоль 9
    10. Вывести в консоль 0
3. Вызовите объявленные функции в таком порядке, чтобы на экране отобразился номер 88005553535.
```
def print_1():
    print(1, end='')

def print_2():
    print(2, end='')

def print_3():
    print(3, end='')

def print_4():
    print(4, end='')

def print_5():
    print(5, end='')

def print_6():
    print(6, end='')

def print_7():
    print(7, end='')

def print_8():
    print(8, end='')

def print_9():
    print(9, end='')

def print_0():
    print(0, end='')

print_8() 
print_8()
print_0()
print_0()
print_5()
print_5()
print_5()
print_3()
print_5()
print_3()
print_5()
```
### **[Задание 8](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_1/lesson_1_task_8.py "Задание 8"). Параметризация функций**

1. Создайте файл lesson_1_task_8.py.
2. Создайте функцию, которая принимает на вход параметр num и печатает этот параметр в консоль.
3. Вызовите эту функцию 11 раз так, чтобы в консоль вывелся номер 88005553535.
```
def number(num):
    print(num)

number(8)
number(8)
number(0)
number(0)
number(5)
number(5)
number(5)
number(3)
number(5)
number(3)
number(5)
```
