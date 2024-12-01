# урок "Пространство имён"
print('Задача "Счётчик вызовов": ')

calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    s_info = (len(string), string.upper(), string.lower())
    return(s_info)

def is_contains(string, list_to_search):
    count_calls()
    for elem in list_to_search:
        new_list = elem.lower()

    if string.lower() in new_list:
        return(True)
    else:
        return(False)
    count_calls()

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
