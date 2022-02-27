# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»
# Задача №1

def get_shop_list_by_dishes(dishes_: list, person_count_=1):
    shop_list = dict()
    for dishes_in in dishes_:
        for dishes_dict in cook_book:
            if dishes_dict == dishes_in:
                for ingredients_list in cook_book[dishes_dict]:
                    if ingredients_list['ingredient_name'] not in shop_list.keys():
                        shop_list[ingredients_list['ingredient_name']] = \
                            {key_ing: value_ing.strip() for key_ing, value_ing in ingredients_list.items() if
                             key_ing in ['measure']}
                        shop_list[ingredients_list['ingredient_name']]['quantity'] = \
                            int(ingredients_list['quantity'].strip()) * person_count_
                    else:
                        shop_list[ingredients_list['ingredient_name']]['quantity'] += \
                            int(ingredients_list['quantity'].strip()) * person_count_
    return shop_list


cook_book = {}
count = 0
type_ingredients = ['ingredient_name', 'quantity', 'measure']
line_dishes = str()
with open('recipes.txt') as file:
    for line in file:
        if len(line.strip()) == 0:
            count = 0
        elif count == 0 and line.strip().isnumeric() is False:
            line_dishes = line.strip()
            cook_book[line.strip()] = []  # Добавление нового блюда
        elif line.strip().isnumeric() is True:
            count = int(line.strip())
        else:
            cook_book[line_dishes].append(dict(zip(type_ingredients, line.strip().split('|'))))
            count -= 1

print('Словарь cook_book:')
for dishes in cook_book:
    print(dishes)
    for ingredients in cook_book[dishes]:
        print(ingredients)

# Задача №2
shop_list_by_dishes = get_shop_list_by_dishes(['Омлет', 'Омлет'], 3)
# shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(f'\nЗаказ продуктов на shop_list_by_dishes:')
for i in shop_list_by_dishes:
    print(f'{i}: {shop_list_by_dishes[i]}')
