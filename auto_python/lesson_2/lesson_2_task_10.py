def bank(X, Y):
    balance = X
    for year in range(Y):
        balance += balance * 0.1
    return balance

X = float(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада (в годах): "))

result = bank(X, Y)
print("Сумма на счету после", Y, "лет:", result)