import unittest

from .game import Room
from .game import Game


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.x = 5
        self.y = 4
        self.name = "Room to test your unit"
        self.description = "You see units standing, ready for test."
        self.exits = ['This way', 'That way']
        self.room = Room(self.x, self.y, self.name, self.description, self.exits)

    def test_str(self):
        expected = f'{self.name}\n{self.description}'
        result = self.room.__str__()
        self.assertEqual(expected, result)

    def test_check_exit_positive(self):
        result = self.room._check_exit('This way')
        self.assertTrue(result)

    def test_check_exit_negative(self):
        result = self.room._check_exit('No way')
        self.assertFalse(result)


class TestGame(unittest.TestCase):
    Directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west": (-1, 0),
        "east": (1, 0)
    }

    def setUp(self):
        self.player_x = 0
        self.player_y = 0
        self.map = {(0, -1): [0, -1, "Second room", "", ["south"]],
                    (0, 0): [0, 0, "Main room", "", ["north"]]}
        self.current_room = [0, -1, "Second room", "", ["south"]]
        self.game = Game(self.map)

    def test_move(self):
        expected = self.game._look_at(self.current_room)
        result = self.game._move(0, -1)
        self.assertEqual(expected, result)

    def test_get_room(self):
        expected = self.current_room
        result = self.game._get_room(0, -1)
        self.assertEqual(expected, result)

    def test__look_at(self):
        expected = None
        result = self.game._look_at(self.current_room)
        self.assertEqual(expected, result)

    def test_check_parse_negative(self):
        result = self.game._parse('go')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
