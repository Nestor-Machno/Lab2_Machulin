x = {
    'км': 1000,
    'м': 1,
    'см': 0.01,
    'мм': 0.001,
    'мили': 1609.34,
    'ярды': 0.9144
}
print("Единицы измерения:", ", ".join(x.keys()))
from_unit = input("Из какой единицы вы хотите конвертировать? ")
to_unit = input("В какую единицу вы хотите конвертировать? ")
value = float(input(f"Введите ваше значение в {from_unit}: "))
result = value * x[from_unit] / x[to_unit]
print(f"\nРезультат: {value} {from_unit} = {result:.2f} {to_unit}")
