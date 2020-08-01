import unittest
from display_handler import DisplayHandler
from folder_handler import FolderHandler
import curses
from config import (
    colors,
    selected_background,
    default_background,
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
        folder = FolderHandler(self.root_test_folder)
        self.display = DisplayHandler(folder)

    # test interface generation on example folder
    def test_interface_string(self):
        interface_strings = self.display.folders_elements_format(1)
        correct_list = [
            ('file1.txt', curses.COLOR_YELLOW, curses.COLOR_BLACK),
            ('file2.txt', curses.COLOR_YELLOW, curses.COLOR_BLUE),
            ('Folder1', curses.COLOR_GREEN, curses.COLOR_BLACK),
            ('Folder2', curses.COLOR_GREEN, curses.COLOR_BLACK)
        ]
        self.assertEqual(correct_list, interface_strings)

    # test interface generation on example folder txt files only
    def test_interface_filtered_string(self):
        interface_strings = self.display.folders_elements_format(1, 'txt')
        correct_list = [
            ('file1.txt', curses.COLOR_YELLOW, curses.COLOR_BLACK),
            ('file2.txt', curses.COLOR_YELLOW, curses.COLOR_BLUE),
        ]
        self.assertEqual(correct_list, interface_strings)


    # test path with colors
    def test_path_and_colors(self):
        path_line = self.display.path_format()
        self.assertEqual(path_line,(self.root_test_folder,curses.COLOR_WHITE, curses.COLOR_BLACK))


if __name__ == '__main__':
    unittest.main()
