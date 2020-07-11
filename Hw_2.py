def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    biggest_ints = sorted([num for num in set(input_list)])

    return biggest_ints[-3:]


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """

    lowest_int_index = input_list.index(min(input_list))

    return lowest_int_index  # <- f"Lowest index is: {lowest_int_index}"


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    reversed = input_list[::-1]

    return reversed


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = [k for k in dict1.keys() if k in dict2.keys()]

    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    student_list.sort(key=lambda x: x['age'])

    sorted_dict = {}

    for data in student_list:
        if data.get('city') in sorted_dict.keys():
            sorted_dict[data.get('city')].append(data)
            data.pop('city')
        else:
            sorted_dict[data.get('city')] = []
            sorted_dict[data.get('city')].append(data)
            data.pop('city')

    return sorted_dict

