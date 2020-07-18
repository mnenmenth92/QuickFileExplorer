import unittest
from folder_handler import FolderHandler

'''
to run this tests create on C:/ drive TestFolder
TestFolder should contain two folders: Folder1 and Folder2
and two files file1.txt and file2.txt
'''

# folder handling tests
class FileExplorerTest(unittest.TestCase):

    # test listing of empty folder
    def test_list_empty_folder(self):
        folder = FolderHandler('C:\\TestFolder\\Folder1')
        self.assertEqual({}, folder.get_content())

    # test listing of nonempty folder, check Folder
    def test_list_folder(self):
        folder = FolderHandler('C:\\TestFolder')
        whole_dic = folder.get_content()
        self.assertEqual('folder',whole_dic['Folder1'])

    # test listing of nonempty folder, check file
    def test_list_file(self):
        folder = FolderHandler('C:\\TestFolder')
        whole_dic = folder.get_content()
        self.assertEqual('.txt',whole_dic['file1.txt'])


    # test type checking if folder
    def test_if_element_is_folder(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertTrue(folder.if_element_is_folder('Folder2'))

    # test type checking if file
    def test_if_element_is_file(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertFalse(folder.if_element_is_folder('filet1.txt'))

    # test type string checking folder
    def test_element_type_folder(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertEqual('folder', folder.element_type_string('Folder1'))

    # test type string checking empty name
    def test_element_type_file_empty_name(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertEqual('', folder.element_type_string(''))

    # test type string checking file
    def test_element_type_file(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertEqual('.txt', folder.element_type_string('file1.txt'))

    # test type string checking with dot on begging
    def test_element_type_file_dot_on_start(self):
        folder = FolderHandler('C:\\TestFolder')
        self.assertEqual('', folder.element_type_string('.file3'))




if __name__ == '__main__':
    unittest.main()