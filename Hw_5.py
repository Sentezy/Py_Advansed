# Напишите функцию, которая читает и распечатывает текстовый файл.
# Напишите декоратор к этой функции, который печатает название файла и количество слов в нем

import os       


def counter(func):
    def wrapper(*args):
        
        return f"File name : {args[0].split(os.sep)[-1]}    " \
               f"Word count : {len(func(*args).split())}" \
               f"\n{func(*args)}"  # <- Если надо текст файла

    return wrapper


@counter
def file_reader(path):
    with open(path, "r", encoding="utf-8") as data:
        return data.read()


