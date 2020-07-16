# Напишите функцию, которая читает и распечатывает текстовый файл.
# Напишите декоратор к этой функции, который печатает название файла и количество слов в нем

import os        # <- Только ради правильного сепаратора OS


def counter(func):
    def wrapper(*args):
        file_name = args[0].split(os.sep)[-1]
        word = len(func(*args).split())
        return f"File name : {file_name}    " \
               f"Word count : {word}" \
               f"\n{func(*args)}"  # <- Если надо текст файла

    return wrapper


@counter
def file_reader(path):
    with open(path, "r", encoding="utf-8") as data:
        return data.read()


