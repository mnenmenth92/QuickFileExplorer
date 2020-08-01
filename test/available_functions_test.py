import unittest
import curses
from available_functions import OneFunction, Backspace, Character
from user_handler import UserHandler

class FunctionsTest(unittest.TestCase):
    """
    to be tested from terminal

    """

    # setup tests
    def setUp(self):
        stdscr = curses.initscr()
        self.user = UserHandler(stdscr)
        self.functions_dic = {
            'backspace': self.set_backspace,
            'character': self.set_character
        }

    # end test
    def tearDown(self):
        curses.endwin()

    # set backspace as function
    def set_backspace(self):
        self.function = Backspace(self.user)

    # set character as function
    def set_character(self):
        self.function = Character(self.user)

    # run selected function selection
    def run_function(self, name):
        self.functions_dic[name]()

    # check if selected func return correct result for given int value
    def check_int(self, func_name, int_value, result):
        self.run_function(func_name)
        if result:
            self.assertTrue(self.function.check_sign(int_value))
        else:
            self.assertFalse(self.function.check_sign(int_value))

    # test backspace function with correct int
    def test_backspace_int_true(self):
        self.check_int('backspace', 8, True)  # 8 - backspace

    # test backspace function with incorrect int
    def test_backspace_int_false(self):
        self.check_int('backspace', 97, False)  # 97 - a

    # test character input function with correct input
    def test_character_true(self):
        self.check_int('character', 97, True)  # 97 - a

    # test character input function with incorrect input
    def test_character_false(self):
        self.check_int('character', 8, False)  # 8 - backspace

    # test backspace output
    def test_backspace_output(self):
        self.user.input_string = 'test_string'
        self.function = Backspace(self.user)
        self.function.run(8)
        self.assertEqual(self.user.input_string, 'test_strin')

    # test backspace output
    def test_character_output(self):
        self.user.input_string = 'test_string'
        self.function = Character(self.user)
        self.function.run(97)
        self.assertEqual(self.user.input_string, 'test_stringa')



if __name__ == '__main__':
    unittest.main()