# Дополнительное практическое задание по модулю: "Основные операторы"
# Задание "Слишком древний шифр":

n = 15

print("Число из первой вставки: ", n)
numbers = []

for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            numbers.append(str(i) + str(j))

password = ''.join(numbers)

print("Нужный пароль: ", password)
