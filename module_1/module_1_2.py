#Напишите 4 переменных которые буду обозначать следующие данные:
#Количество выполненных ДЗ (запишите значение 12)
#Количество затраченных часов (запишите значение 1.5)
#Название курса (запишите значение 'Python')
#Время на одно задание (вычислить используя 1 и 2 переменные)
#Выведите на экран(в консоль), используя переменные, следующую строку:
#Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

#Количество выполненных ДЗ
homework_number = 12
#Количество затраченных часов
spent_hours = 1.5
#Название курса
course_name = "Python"
# Время на одно задание
time_for_one_task = spent_hours / homework_number
#первый неправильный вариант вывода, оставляю, чтоб понять почему
print("Курс:", course_name, ",", "всего задач: ", homework_number, ", затрачено часов: ",
      spent_hours, ", среднее время выполнения", time_for_one_task, "часа.")
#второй верный вариант для проверки
print(f"Курс: {course_name}, всего задач:{homework_number}, затрачено часов: {spent_hours}"
      f", среднее время выполнения {time_for_one_task} часа.")
#строка из задания для контроля
print("Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.")
