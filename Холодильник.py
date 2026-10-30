import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

items = {}


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


#Закомментировал тестирование(на случй автоматической проверки)

# Тестирование
# today = datetime.date.today()
# yesterday = (today - datetime.timedelta(days=1)).strftime(DATE_FORMAT)
# tomorrow = (today + datetime.timedelta(days=1)).strftime(DATE_FORMAT)
# in_100_years = today.replace(year=today.year + 100).strftime(DATE_FORMAT)

# add(items, 'Яйца', Decimal('10'), '2023-9-30')
# add(items, 'Яйца', Decimal('3'), '2023-10-15')
# add(items, 'Вода', Decimal('2.5'))
# add(items, 'Молоко', Decimal('1'), yesterday)
# add(items, 'Молоко', Decimal('2'), tomorrow)
# add(items, 'Сыр', Decimal('0.3'), in_100_years)

# add_by_note(items, 'Яйца гусиные 4 2023-07-15')
# add_by_note(items, 'Пельмени Универсальные 0.5 2023-09-30')
# add_by_note(items, 'Пельмени Универсальные 2 2023-10-28')
# add_by_note(items, 'Морковь 5')

# show_fridge(items)

# print()
# show_find(items, 'яйц')
# show_find(items, 'Вода')
# show_find(items, 'мясо')

# print()
# show_amount(items, 'яйца')
# show_amount(items, 'пельмени')
# show_amount(items, 'морковь')
# show_amount(items, 'молоко')
# show_amount(items, 'рыба')
