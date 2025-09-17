resistances = list(map(float, input("Введите сопротивления элементов через пробел: ").split()))

# Инициализируем переменную для суммы обратных сопротивлений
sum_inverse = 0

# Проходим по каждому сопротивлению и находим его обратное
for R in resistances:
    sum_inverse += 1 / R

# Находим общее сопротивление цепи
if sum_inverse != 0:
    R_total = 1 / sum_inverse
else:
    pass

# Выводим результат
print("Общее сопротивление цепи:", R_total, "Ом")
