# # Дополнительное практическое задание по модулю: "Базовые структуры данных.
# print('Задание "Средний балл": ')
#
# # дано:
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# average_grades = []
# for i in range(len(grades)):
#     average_grades.append(sum(grades[i])/len(grades[i]))
#
# students = list(students)
# students.sort()
#
# ratings = {}
# ratings = dict(zip(students, average_grades))
# print(ratings) #искомый словарь

example = [14, 23, 32, 41]
print(example[0])
print(example[-1])
print(example[int(len(example) / 2):])
print(example[::-1])
print(example[::2])
