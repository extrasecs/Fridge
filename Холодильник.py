import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    # если такого продукта ещё нет, создаём для него пустой список партий
    if title not in items:
        items[title] = []

    # если срок годности указан, превращаем строку в дату
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, DATE_FORMAT).date()

    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    parts = note.split()

    # если в последней части три числа через дефис, то это дата
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    result = []
    for title in items:
        if needle.lower() in title.lower():
            result.append(title)
    return result


def amount(items, needle):
    total = Decimal('0')
    for title in find(items, needle):
        for batch in items[title]:
            total += batch['amount']
    return total


#Функции ниже я закомментировал, тк часть из них не является частью задания, хотелось просто сделать вывод покрасивее. 
#Закомментировал и тестирование(на случй автоматической проверки)


# Функции для красивого вывода
# def show_fridge(items):
#     print('В холодильнике лежит:')
#     for title in items:
#         print(f'{title}:')
#         for batch in items[title]:
#             if batch['expiration_date'] is None:
#                 date_text = 'срок годности не указан'
#             else:
#                 date_text = 'годен до ' + batch['expiration_date'].strftime('%d.%m.%Y')
#             print(f'  - {batch["amount"]}, {date_text}')


# def show_find(items, needle):
#     found = find(items, needle)
#     if found:
#         print(f'По запросу "{needle}" найдено: {", ".join(found)}')
#     else:
#         print(f'По запросу "{needle}" ничего не найдено')


# def show_amount(items, needle):
#     total = amount(items, needle)
#     if total == 0:
#         print(f'Продукта "{needle}" в холодильнике нет')
#     else:
#         print(f'Всего "{needle}": {total}')


# Тестирование
# today = datetime.date.today()
# yesterday = (today - datetime.timedelta(days=1)).strftime(DATE_FORMAT)
# tomorrow = (today + datetime.timedelta(days=1)).strftime(DATE_FORMAT)
# in_100_years = today.replace(year=today.year + 100).strftime(DATE_FORMAT)

# add(goods, 'Яйца', Decimal('10'), '2023-9-30')
# add(goods, 'Яйца', Decimal('3'), '2023-10-15')
# add(goods, 'Вода', Decimal('2.5'))
# add(goods, 'Молоко', Decimal('1'), yesterday)
# add(goods, 'Молоко', Decimal('2'), tomorrow)
# add(goods, 'Сыр', Decimal('0.3'), in_100_years)

# add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
# add_by_note(goods, 'Пельмени Универсальные 0.5 2023-09-30')
# add_by_note(goods, 'Пельмени Универсальные 2 2023-10-28')
# add_by_note(goods, 'Морковь 5')

# show_fridge(goods)

# print()
# show_find(goods, 'яйц')
# show_find(goods, 'Вода')
# show_find(goods, 'мясо')

# print()
# show_amount(goods, 'яйца')
# show_amount(goods, 'пельмени')
# show_amount(goods, 'морковь')
# show_amount(goods, 'молоко')
# show_amount(goods, 'рыба')