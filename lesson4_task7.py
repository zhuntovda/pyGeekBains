def factorial_gen(n):
    factOrder = 1
    for el in range(1, n+1):
        factOrder = factOrder * el
        yield factOrder

print([el for el in factorial_gen(int(input("Введите число, для получение факториалов до него: ")))])
