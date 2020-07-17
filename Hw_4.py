# 1. Напишите функцию, которая возвращает список файлов из директории.
#
# 2. Напишите декоратор для этой функции, который распечатает все файлы с
#
# раcширением .log из найденных

import os


def file_reader(func):
    def wrapper(*args):

        for file in func(*args):
            if file.endswith('.log'):
                with open(f"{args[0]}{file}", "r", encoding="utf-8") as data:
                    print(data.read())

        return f"Files in path: {func(*args)}"  
                                               
    return wrapper


@file_reader
def file_finder(path):
    for path, dirs, files in os.walk(path):
        return files
