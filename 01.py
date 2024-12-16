from math import prod  

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

floats_cubed = [round(x ** 3, 3) for x in floats]

long_names = [name for name in names if len(name) >= 5]

numbers_product = prod(numbers)

print("Список чисел в третьей степени:", floats_cubed)
print("Список длинных имен:", long_names)
print("Произведение чисел:", numbers_product)