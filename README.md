# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

Необходимо написать программу для кулинарной книги.
Список рецептов должен храниться в отдельном файле в следующем формате:
```python
Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения
...
```

Пример файла:
```python
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
```

## Задание № 1. Словарь 
Класс Mentor - родительский класс, а от него реализовано наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Имя, фамилия и список закрепленных курсов реализовано на уровне родительского класса.
Должен получится следующий словарь
```python
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
```

## Задание № 2. 
# Задание №1,2 файл main.py
Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

```python
get_shop_list_by_dishes(dishes, person_count)
```

На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

```python
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
```

Должен быть следующий результат:
```python
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
```

Обратите внимание, что ингредиенты могут повторяться

## Задание № 3. 
# Задание №3 файл hw3.py
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять тут

Необходимо объединить их в один по следующим правилам:

Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
Пример Даны файлы: 
```python
1.txt

Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```
```python
2.txt

Строка номер 1 файла номер 2
Итоговый файл:
```
```python
2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```



