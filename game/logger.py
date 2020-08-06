import logging


class MyLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        self.log = logging.getLogger('__name__')
        self.log.setLevel(logging.INFO)
        self.fh = logging.FileHandler('game_log.txt')
        self.fh.setLevel(logging.INFO)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)
        self.log.addHandler(self.fh)
        self.log.addHandler(self.ch)

    def info(self, msg, **kwargs):
        self.log.info(msg)

    def warning(self, msg, **kwargs):
        self.log.warning(msg)

    def error(self, msg, **kwargs):
        self.log.error(msg)

    def critical(self, msg, **kwargs):
        self.log.critical(msg)


if __name__ == '__main__':
    log = MyLogger('Log')

    def func(a, b):
        log.error('lol', )
        return a + b


    print(func(1, 3))
