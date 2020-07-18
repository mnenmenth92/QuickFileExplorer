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
to run this tests create on C:/ drive TestFolder
TestFolder should contain two folders: Folder1 and Folder2
and two files file1.txt and file2.txt
'''


# display handling tests
class DisplayHandlerTest(unittest.TestCase):

    # test interface generation on example folder
    def test_interface_string(self):
        folder = FolderHandler('C:\\TestFolder')
        display = DisplayHandler(folder)
        interface_strings = display.interface_stirngs('', 1)
        correct_list = [
                        link_format + 'C:\\TestFolder',
                        reset_format + '',
                        '',
                        reset_background + colors['.txt'] + 'file1.txt',
                        selected_background + colors['.txt'] + 'file2.txt',
                        reset_background + colors['folder'] + 'Folder1',
                        reset_background + colors['folder'] + 'Folder2',
                        ]
        self.assertEqual(correct_list, interface_strings)

    # just to have printed the example interface
    def test_print_interface(self):
        folder = FolderHandler('C:\\TestFolder')
        display = DisplayHandler(folder)
        display.print_interface('', 1)
        pass


if __name__ == '__main__':
    unittest.main()