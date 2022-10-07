def get_user(technic):
    result = {}
    for order in technic:
        if f'{order[2]} {order[3]}' not in result:
            result[f'{order[2]} {order[3]}'] = [f'{order[0]} - {order[1]}']
        else:
            result[f'{order[2]} {order[3]}'].append(f'{order[0]} - {order[1]}')
    return result


def get_info():
    technic = [
        ('Ноутбук', 1500, 'Татьяна', '89002001020'),
        ('Смартфон', 500, 'Анна', '89202202325'),
        ('Проектор', 300, 'Андрей', '89505205656'),
        ('Принтер', 750, 'Игорь', '89303303236'),
        ('Планшет', 2300, 'Игорь', '89303303236'),
        ('Смартфон', 1000, 'Андрей', '89505205656'),
        ('Ноутбук', 4800, 'Татьяна', '89002001020'),
        ('Наушники', 780, 'Марина', '89562002350'),
        ('Сканер', 550, 'Сергей', '89808564559'),
        ('Планшет', 1200, 'Анна', '89202202325'),
        ('Ноутбук', 1100, 'Игорь', '89303303236'),
        ('Смартфон', 3500, 'Татьяна', '89002001020'),
    ]

    users_dict = get_user(technic)

    result = ''
    for key, value in users_dict.items():
        items = '; '.join(str(x) for x in value)
        result += f'{key}: {items}\n'

    return result
print(get_info())