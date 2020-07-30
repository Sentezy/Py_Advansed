import random


class Field:
    """
    class for generating player fields
    """

    def __init__(self):
        self.battle_map = list()
        self.move_map = list()

    def gen_battle(self):
        lst = list()
        for i in range(92):
            lst.append('~')
        for i in range(8):
            lst.append('O')
        random.shuffle(lst)
        start = 0
        for i in range(10):
            stop = start + len(lst[i::10])
            self.battle_map.append(lst[start:stop])
            start = stop

        return self.battle_map

    def gen_move(self):
        lst = (['~' for _ in range(10)] for _ in range(10))
        for i in lst:
            self.move_map.append(i)

        return self.move_map


class Game:

    def __init__(self, b_map1, m_map1, b_map2, m_map2, player1, player2):
        """
            :param b_map1: battle map for 1st player
            :param m_map1: map for 1st player moves
            :param b_map2: battle map for 2nd player
            :param m_map2: map for 2nd player moves
            :param player1: 1st player name
            :param player2: 2nd player name
        """
        self.b_map1 = b_map1
        self.m_map1 = m_map1
        self.b_map2 = b_map2
        self.m_map2 = m_map2
        self.player1 = player1
        self.player2 = player2
        self.count1 = 8
        self.count2 = 8

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, player1):
        self._player1 = player1

    @property
    def player2(self):
        return self._player2

    @player2.setter
    def player2(self, player2):
        self._player2 = player2

    def pl1_move(self, x, y):
        if 'O' in self.b_map2[x - 1][y - 1]:
            print("\nYou got it!\n")
            self.b_map2[x - 1][y - 1] = 'X'
            self.m_map1[x - 1][y - 1] = 'X'
            self.count1 -= 1
        if self.count1 == 0:
            return False, print(f'Game Over! -> {self.player1} win!')
        if '~' in self.b_map2[x - 1][y - 1]:
            print("\nYou miss!\n")
            self.b_map2[x - 1][y - 1] = '*'
            self.m_map1[x - 1][y - 1] = '*'
            return *self.b_map1, *self.m_map1
        else:
            return *self.b_map1, *self.m_map1

    def pl2_move(self, x, y):
        if 'O' in self.b_map1[x - 1][y - 1]:
            print("\nYou got it!\n")
            self.b_map1[x - 1][y - 1] = 'X'
            self.m_map2[x - 1][y - 1] = 'X'
            self.count2 -= 1
        if self.count2 == 0:
            return False, print(f'\nGame Over! -> {self.player2} win!')
        if '~' in self.b_map1[x - 1][y - 1]:
            print('\nYou miss!\n')
            self.b_map1[x - 1][y - 1] = '*'
            self.m_map2[x - 1][y - 1] = '*'
            return *self.b_map2, *self.m_map2
        else:
            return *self.b_map2, *self.m_map2

    def run(self):
        while True:
            print("{a:<22}{b:>22}\n".format(a=self.player1, b=self.player2))
            for i in range(10):
                print(*self.b_map1[i], '\t', *self.m_map1[i])
            while True:
                x, y = map(int, input("Input x,y coordinates >>>").split(','))
                if 1 <= x <= 10 and 1 <= y <= 10:
                    x = x
                    y = y
                    break
                else:
                    print("Invalid data, try again")
            if False in self.pl1_move(x, y):
                break
            print("{a:<22}{b:>22}\n".format(a=self.player2, b=self.player1))
            for i in range(10):
                print(*self.b_map2[i], '\t', *self.m_map2[i])
            while True:
                x, y = map(int, input("Input x,y coordinates >>>").split(','))
                if 1 <= x <= 10 and 1 <= y <= 10:
                    x = x
                    y = y
                    break
                else:
                    print("Invalid data, try again")
            if False in self.pl2_move(x, y):
                break


f_pl1 = Field()
f_pl2 = Field()
print("Welcome to'Sea Battle\n")
p_1 = str(input("\nInput 1st player name >>>"))
p_2 = str(input("\nInput 2nd player name >>>"))
game = Game(f_pl1.gen_battle(), f_pl1.gen_move(),
            f_pl2.gen_battle(), f_pl2.gen_move(), p_1, p_2)

print('\nLets battle start!!!\n')

game.run()
input('\nPress "Enter" to exit')
