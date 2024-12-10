# Дополнительное практическое задание по модулю: "Подробнее о функциях."
print('Задание "Раз, два, три, четыре, пять .... Это не всё?":')
global summa

def calculate_structure_sum(data):
    summa = 0

    for elem in data:
        if isinstance(elem, (list, tuple, set)):
            summa += calculate_structure_sum(elem)
        elif isinstance(elem, dict):
            summa += calculate_structure_sum(elem.items())
        elif isinstance(elem, (int, float)):
            summa += elem
        elif isinstance(elem, str):
            summa += len(elem)
    return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
