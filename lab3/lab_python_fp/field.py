def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            if item[args[0]] is not None: yield item[args[0]]
    elif len(args) > 1:
        for item in items:
            # Проверим, не являются ли все значения None
            count = 0
            for arg in args:
                if item[arg] is None: count += 1
            # Если нет, продолжаем
            if count != len(args):
                # Создаем словарь
                result = {}
                # Добавляем в него != None элементы
                for arg in args:
                    if item[arg] is not None:
                       result[arg] = item[arg]
                # Возвращаем словарь
                yield result
                