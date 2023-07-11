### **Задание 1. Создание класса**

1. Создайте файл [user.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/user.py "user.py").
2. В файле объявите класс `User`.
3. Объявите в классе конструктор.

Конструктор должен принимать на вход 2 параметра:

1. `first_name` — имя.
2. `last_name` — фамилия.

Помните, что все методы класса, включая конструктор, принимают первым параметром `self`.

1. Создайте в классе 3 метода, которые печатают:
    - имя,
    - фамилию,
    - имя и фамилию.
2. Создайте файл [lesson_3_task_1.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/lesson_3_task_1.py 'lesson_3_task_1.py').
3. Импортируйте в него класс `user`.
4. Создайте новый экземпляр `User` и сохраните его в переменную `my_user`.
5. Вызовите все методы у объекта в переменной `my_user`.

### **Задание 2. Список объектов**

1. Создайте файл [smartphone.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/smartphone.py 'smartphone.py').
2. В файле объявите класс `Smartphone`.
3. Объявите в классе конструктор.

Конструктор должен принимать на вход следующие параметры:

- марка телефона,
- модель телефона,
- абонентский номер (”+79…”).
1. Создайте файл [lesson_3_task_2.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/lesson_3_task_2.py 'lesson_3_task_2.py').
2. В файле объявите переменную `catalog`.
3. Переменная хранит в себе список (`[]`).
4. Наполните список пятью разными экземплярами класса `Smartphone`.
5. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.

### **Задание 3. Вложенные классы**

1. В отдельном файле создайте класс [Address](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/address.py 'Address').
2. Класс должен содержать в себе поля:
    - «индекс»,
    - «город»,
    - «улица»,
    - «дом»,
    - «квартира».
3. В отдельном файле создайте класс [Mailing](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/mailing.py 'Mailing') (почтовое отправление).
4. В классе должно быть 4 поля:
    - `to_address` (тип данных `Address`),
    - `from_address` (тип данных `Address`),
    - `cost` (тип данных `число`),
    - `track` (тип данных строка).
5. Создайте файл [lesson_3_task_3.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/lesson_3_task_3.py 'lesson_3_task_3.py').
6. Импортируйте классы `Address` и `Mailing`.
7. В файле создайте экземпляр класса `Mailing`.
8. Заполните поля класса адресами (`to_address` и `from_address`), трек-номером (`track`) и стоимостью (`cost`).
9. Распечатайте в консоль отправление в формате: `Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.`.

Все данные должны получаться из экземпляра `Mailing`.

### **Задание 4. Нарисуйте картинку**

1. Создайте файл [lesson_3_task_4.py](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/lesson_3_task_4.py 'lesson_3_task_4.py').
2. Скопируйте и запустите код:
    
    ```python
    from turtle import *
    
    my_turtle = Turtle()
    my_turtle.speed(0)
    my_turtle.screen.setup(1200, 800)
    
    # Нарисовать квадрат
    def draw_rect(t):
        for x in range(0, 4):
            t.right(90)
            t.forward(100)
    
    # Рисует квадраты в цикле
    for x in range(0, 360):
        draw_rect(my_turtle)
        my_turtle.right(1)
    
    # Необходимо, чтобы окно не закрывалось само, а только по клику
    my_turtle.screen.exitonclick()
    my_turtle.screen.mainloop()
    
    ```
    
3. Изучите структуру кода  на предмет основных блоков.
4. Изучите статьи:
- «**Графика turtle черепашка в питон»:**  http://itrobo.ru/programmirovanie/python/grafika-turtle-cherepashka-v-piton.html
- «****Черепаха (turtle) в python»:**** https://koddom.com/kodim/turtle-python/****.****
1. Напишите код, который рисует изображение любого животного.
2. Поделитесь скриншотом рисунка в чате с коллегами.

[Мой рисунок: Колобок](https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/animal.py 'Колобок')
<div align="center">
<img src = "https://github.com/mranolegprivate/skypro/blob/main/auto_python/lesson_3/Screenshot_3.jpg?raw=true"/>
</div>



