def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    lst = list()
    for i in url_list:
        if "/catalog/" in i:
            lst.append(i)

    result_list = lst
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    res = str

    if len(input_str) % 2 == 0:
        res = input_str[len(input_str) // 2 - 1:
                        len(input_str) // 2 + 1]
    else:
        res = input_str[len(input_str) // 2 - 1:
                        len(input_str) // 2 + 2]

    output_str = res
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    txt = dict()

    for i in input_str.replace(" ", ""):
        txt[i] = txt.get(i, 0) + 1

    output_dict = txt
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    new_str = str1[:len(str1) // 2] + str2 + str1[len(str1) // 2:]

    result_str = new_str
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    from random import randint

    gen_lst = [randint(0, 100) for _ in range(25)]

    sort_lst = [i for i in gen_lst if not i % 2]

    even_int_list = sort_lst
    return even_int_list
