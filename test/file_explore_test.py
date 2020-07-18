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
        folder = FolderHandler('C:\TestFolder\Folder1')
        self.assertEqual([], folder.get_content())

    # test listing of nonempty folder
    def test_list_folder(self):
        folder = FolderHandler('C:\TestFolder')
        self.assertEqual(['file1.txt', 'file2.txt', 'Folder1', 'Folder2'], folder.get_content())



if __name__ == '__main__':
    unittest.main()