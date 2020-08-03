import unittest
from display_handler import DisplayHandler
from folder_handler import FolderHandler
import curses
from config import (
    colors,
    selected_background,
    default_background,
    path_line_num,
    folder_content_line_num,
    type_line_num
)

'''
to run this tests create folder (root_test_folder) with following content
TestFolder should contain two folders: Folder1 and Folder2
and two files file1.txt and file2.txt

default test folder is C:\TestFolder 
'''


# display handling tests
class DisplayHandlerTest(unittest.TestCase):
    # folder with content for below tests
    root_test_folder = 'C:\\TestFolder'

    # set up tests
    def setUp(self):
        stdscr = curses.initscr()
        folder = FolderHandler(self.root_test_folder)
        self.display = DisplayHandler(folder, stdscr)

    # end test
    def tearDown(self):
        curses.endwin()


    # test interface generation on example folder
    def test_interface_string(self):
        interface_strings = self.display.folders_elements_format(1)
        correct_list = [
            ('file1.txt', curses.COLOR_YELLOW, curses.COLOR_BLACK, folder_content_line_num),
            ('file2.txt', curses.COLOR_YELLOW, curses.COLOR_BLUE, folder_content_line_num + 1),
            ('Folder1', curses.COLOR_GREEN, curses.COLOR_BLACK, folder_content_line_num + 2),
            ('Folder2', curses.COLOR_GREEN, curses.COLOR_BLACK, folder_content_line_num + 3)
        ]
        self.assertEqual(correct_list, interface_strings)

    # test interface generation on example folder txt files only
    def test_interface_filtered_string(self):
        interface_strings = self.display.folders_elements_format(1, 'txt')
        correct_list = [
            ('file1.txt', curses.COLOR_YELLOW, curses.COLOR_BLACK, folder_content_line_num),
            ('file2.txt', curses.COLOR_YELLOW, curses.COLOR_BLUE, folder_content_line_num + 1)
        ]
        self.assertEqual(correct_list, interface_strings)


    # test path with colors
    def test_path_and_colors(self):
        path_line = self.display.path_format()
        self.assertEqual(path_line, (self.root_test_folder,curses.COLOR_WHITE, curses.COLOR_BLACK, path_line_num))

    # test type line format
    def test_type_line(self):
        type_line = self.display.type_format()
        self.assertEqual(type_line, ('', curses.COLOR_WHITE, curses.COLOR_BLACK, type_line_num))



if __name__ == '__main__':
    unittest.main()
