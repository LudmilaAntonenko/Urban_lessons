def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"

    print(inner_function())


# inner_function()
# при вызове inner_function вне функции test_function возникает ошибка:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?