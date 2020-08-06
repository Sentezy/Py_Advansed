import logging




class MyLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)

        self.setLevel(logging.INFO)
        fh = logging.FileHandler('game_log.txt')
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.addHandler(fh)
        self.addHandler(ch)
