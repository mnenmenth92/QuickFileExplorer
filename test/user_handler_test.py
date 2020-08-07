import unittest
import curses
from config import default_path
from user_handler import UserHandler
from display_handler import DisplayHandler
from folder_handler import FolderHandler



class UserHandlerTest(unittest.TestCase):

    # setup tests
    def setUp(self):
        stdscr = curses.initscr()
        curses.start_color()

        self.folder_handler = FolderHandler(default_path)
        self.display_handler = DisplayHandler(self.folder_handler, stdscr)
        self.user = UserHandler(self.folder_handler, self.display_handler, stdscr)

    # end test
    def tearDown(self):
        curses.endwin()

    # test storing selected elements
    def test_store_selected_element(self):
        self.user.selected_element_list = []
        self.user.selected_element = 3
        self.user.store_selected_element()
        self.user.selected_element = 2
        self.user.store_selected_element()
        self.user.selected_element = 7
        self.user.store_selected_element()
        self.assertEqual(self.user.selected_element_list, [3, 2, 7])

    # test removing selected element: result
    def test_remove_selected_element_result(self):
        self.user.selected_element_list = [2,8]
        element_num = self.user.remove_selected_element()
        self.assertEqual(element_num, 8)

    # test removing selected element: result, empty list
    def test_remove_selected_element_result_empty_list(self):
        self.user.selected_element_list = []
        element_num = self.user.remove_selected_element()
        self.assertEqual(element_num, 0)


    # test removing selected element: list
    def test_remove_selected_element_list(self):
        self.user.selected_element_list = [2, 5, 8]
        self.user.remove_selected_element()
        self.assertEqual(self.user.selected_element_list, [2, 5])

    # test removing from empty list
    def test_remove_selected_element_empty_list(self):
        self.user.selected_element_list = []
        self.user.remove_selected_element()
        self.assertEqual(self.user.selected_element_list, [])