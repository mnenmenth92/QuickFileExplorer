import unittest
from folder_handler import FolderHandler

'''
to run this tests create folder (root_test_folder) with following content
TestFolder should contain two folders: Folder1 and Folder2
and two files file1.txt and file2.txt

default test folder is C:\TestFolder 
'''

# folder handling tests
class FileExplorerTest(unittest.TestCase):
    # folder with content for below tests
    root_test_folder = 'C:\\TestFolder'

    # set up tests
    def setUp(self):
        self.folder = FolderHandler(self.root_test_folder)


    # test listing of empty folder
    def test_list_empty_folder(self):
        folder = FolderHandler(self.root_test_folder + '\\Folder1')
        self.assertEqual({}, folder.get_content())

    # test listing of nonempty folder, check Folder
    def test_list_folder(self):
        whole_dic = self.folder.get_content()
        self.assertEqual('folder', whole_dic['Folder1'])

    # test listing of nonempty folder, check file
    def test_list_file(self):
        whole_dic = self.folder.get_content()
        self.assertEqual('.txt', whole_dic['file1.txt'])

    # test type checking if folder
    def test_if_element_is_folder(self):
        self.assertTrue(self.folder.if_element_is_folder('Folder2'))

    # test type checking if file
    def test_if_element_is_file(self):
        self.assertFalse(self.folder.if_element_is_folder('filet1.txt'))

    # test type string checking folder
    def test_element_type_folder(self):
        self.assertEqual('folder', self.folder.element_type_string('Folder1'))

    # test type string checking empty name
    def test_element_type_file_empty_name(self):
        self.assertEqual('', self.folder.element_type_string(''))

    # test type string checking file
    def test_element_type_file(self):
        self.assertEqual('.txt', self.folder.element_type_string('file1.txt'))

    # test type string checking with dot on begging
    def test_element_type_file_dot_on_start(self):
        self.assertEqual('', self.folder.element_type_string('.file3'))




if __name__ == '__main__':
    unittest.main()