import unittest
from display_handler import DisplayHandler
from folder_handler import FolderHandler
from config import (
    colors,
    selected_background,
    reset_background,
    link_format,
    reset_format)

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
        interface_strings = self.display.interface_strings('', 1)
        correct_list = [
                        link_format + self.root_test_folder,
                        reset_format + '',
                        '',
                        reset_background + colors['.txt'] + 'file1.txt',
                        selected_background + colors['.txt'] + 'file2.txt',
                        reset_background + colors['folder'] + 'Folder1',
                        reset_background + colors['folder'] + 'Folder2',
                        ]
        self.assertEqual(correct_list, interface_strings)

    # test interface generation on example folder
    def test_interface_filtered_string(self):
        interface_strings = self.display.interface_strings('', 1, 'txt')
        correct_list = [
            link_format + self.root_test_folder,
            reset_format + '',
            '',
            reset_background + colors['.txt'] + 'file1.txt',
            selected_background + colors['.txt'] + 'file2.txt',
        ]
        self.assertEqual(correct_list, interface_strings)

    # just to have printed the example interface
    def test_print_interface(self):
        self.display.print_interface('', 1)
        pass


if __name__ == '__main__':
    unittest.main()