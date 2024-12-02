# Домашнее задание по уроку "Распаковка позиционных параметров".
print('Задача "Распаковка":')

print("1.Функция с параметрами по умолчанию:")

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 2, 3)
print_params(b = 25)
print_params(c = [1,2,3])
#Все вызовы работают, т.к. изначально функция с параметрами по умолчанию

print("2.Распаковка параметров:")

values_list = [True, 'string', 3]
values_dict = {'a': 1, 'b': True, 'c': (1, 2)}

print_params(*values_list)
print_params(**values_dict)

print("3.Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)