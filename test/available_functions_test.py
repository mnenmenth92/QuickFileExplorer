import unittest
import curses
from available_functions import OneFunction, Backspace, Character
from user_handler import UserHandler

class FunctionsTest(unittest.TestCase):
    '''
    to be tested from terminal

    '''

    functions_dic = {
        'backspace': set_backspace,
        'character': set_character

    }

    # setup tests
    def setUp(self):
        stdscr = curses.initscr()
        self.user = UserHandler(stdscr)

    # end test
    def tearDown(self):
        curses.endwin()

    # set backspace as function
    def set_backspace():
        self.function = Backspace(self.user)
    #set character as function
    def set_character():
        self.function = Character(self.user)

    # check if selected func return correct result for given int value
    def check_int(self, func_name, int_value, result):
        pass


    # test backspace function with correct int
    def test_backspace_int_true(self):
        self.function = Backspace(self.user)
        self.assertTrue(self.function.check_sign(8))  # backspace

    # test backspace function with incorrect int
    def test_backspace_int_false(self):
        self.function = Backspace(self.user)
        self.assertFalse(self.function.check_sign(97))  # 97 - 'a'

    # test character input function with correct input
    def test_character_true(self):
        self.function = Character(self.user)
        self.assertTrue(self.function.check_sign(97))  # 97 - 'a'

    # test character input function with incorrect input
    def test_character_false(self):
        self.function = Character(self.user)
        self.assertFalse(self.function.check_sign(8))  # 8 - backspace


    # test backspace output
    def test_backspace_output(self):
        self.user.input_string = 'test_string'
        self.function = Backspace(self.user)
        self.function.run()
        self.assertEqual(self.user.input_string, 'test_strin')



if __name__ == '__main__':
    unittest.main()