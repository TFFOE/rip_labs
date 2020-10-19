def print_result(func_to_print):

    def decorated_func(arg):
        # Вывод названия функции
        print(func_to_print.__name__)

        # Исполнение фукнции
        result = func_to_print(arg)

        # Вывод результата в зависимости от его типа
        if type(result) is list:
            for item in result:
                print(item)
        elif type(result) is dict:
            for key, item in result.items():
                print(f'{key} = {item}')
        else:
            print(result)

        # Возвращение значения функции
        return result
        
    return decorated_func