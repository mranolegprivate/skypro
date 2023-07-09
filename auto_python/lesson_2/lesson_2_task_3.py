import math # Модуль math предоставляет функции для округления чисел:

side1 = input()

side = float(side1)

def square(side):
    if isinstance(side, int):
        return side * side
    else:
        return math.ceil(side * side) # math.ceil(x) — округляет число вверх до ближайшего целого числа.

result = square(side)
print(f"площадь квадрата {side}: {result}")