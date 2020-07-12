# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами,
# она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.

def do_cache(maxsize):
    def dec_value(func):
        value = {}

        def wrapper(*args):

            if args in value:
                return value[args]
            if maxsize == len(value):
                value.popitem()
                result = func(*args)
                value[args] = result
                return result
            if args not in value:
                result = func(*args)
                value[args] = result
                return result

            return value

        return wrapper

    return dec_value


@do_cache(maxsize=3)
def get_value(a, b):
    return a ** b
