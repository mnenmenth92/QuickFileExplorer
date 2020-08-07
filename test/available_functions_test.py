import unittest
import curses
import importlib
import inspect
from user_handler import UserHandler
from folder_handler import FolderHandler
from display_handler import DisplayHandler
from config import default_path


class FunctionsTest(unittest.TestCase):
    """
    to be tested from terminal

    """

    # setup tests
    def setUp(self):
        stdscr = curses.initscr()
        curses.start_color()

        self.folder_handler = FolderHandler(default_path)
        self.display_handler = DisplayHandler(self.folder_handler, stdscr)
        self.user = UserHandler(self.folder_handler, self.display_handler, stdscr)
        self.functions_dic = {}
        for name, cls in inspect.getmembers(importlib.import_module("available_functions"), inspect.isclass):
            function = cls(self)

            self.functions_dic.update({type(function).__name__: function})

    # end test
    def tearDown(self):
        curses.endwin()

    # check if selected func return correct result for given int value
    def check_int(self, func_name, int_value, result):
        function = self.functions_dic[func_name]
        if result:
            self.assertTrue(function.check_sign(int_value))
        else:
            self.assertFalse(function.check_sign(int_value))

    # test backspace function with correct int
    def test_backspace_int_true(self):
        self.check_int('Backspace', 8, True)  # 8 - backspace

    # test backspace function with incorrect int
    def test_backspace_int_false(self):
        self.check_int('Backspace', 97, False)  # 97 - a

    # test character input function with correct input
    def test_character_true(self):
        self.check_int('Character', 97, True)  # 97 - a

    # test character input function with incorrect input
    def test_character_false(self):
        self.check_int('Character', 8, False)  # 8 - backspace

    # test up input function with correct input
    def test_up_true(self):
        self.check_int('Up', 259, True)  # 259 - up

    # test up input function with incorrect input
    def test_up_false(self):
        self.check_int('Up', 8, False)  # 8 - backspace

    # test down input function with correct input
    def test_down_true(self):
        self.check_int('Down', 258, True)  # 258 - down

    # test down input function with incorrect input
    def test_down_false(self):
        self.check_int('Down', 8, False)  # 8 - backspace

    # test right input function with correct input
    def test_right_true(self):
        self.check_int('Right', 261, True)  # 261 - right

    # test right input function with incorrect input
    def test_right_false(self):
        self.check_int('Right', 8, False)  # 8 - backspace

    # test left input function with correct input
    def test_left_true(self):
        self.check_int('Left', 260, True)  # 260- left

    # test left input function with incorrect input
    def test_left_false(self):
        self.check_int('Left', 8, False)  # 8 - backspace



    # test backspace output
    def test_backspace_output(self):
        function = self.functions_dic['Backspace']
        function.user_handler = self.user
        function.user_handler.input_string = 'test_string'
        function.user_handler.selected_element = 1
        function.run(8)
        self.assertEqual(self.user.input_string, 'test_strin')

    # test backspace output
    def test_character_output(self):
        function = self.functions_dic['Character']
        function.user_handler = self.user
        function.user_handler.input_string = 'test_string'
        function.user_handler.selected_element = 1
        function.run(97)
        self.assertEqual(self.user.input_string, 'test_stringa')


if __name__ == '__main__':
    unittest.main()
