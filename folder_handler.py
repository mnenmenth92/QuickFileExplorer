import os

# folder handling
class FolderHandler:
    def __init__(self, default_path):
        self.current_path = default_path

    # list current folder
    def get_content(self):
        content_list = os.listdir(self.current_path)
        result = {i: self.element_type_string(i) for i in content_list}
        return result

    # check if element is folder
    # True is folder, false is file
    def if_element_is_folder(self, name):
        new_path = os.path.join(self.current_path, name)
        return os.path.isdir(new_path)

    # returns element type stirng
    # 'folder' for folders
    # '.<extension>' for extension e.g. '.txt'
    def element_type_string(self, name):
        if self.if_element_is_folder(name) and name:
            return 'folder'
        if name:
            name_elements = name.split('.')
            if name_elements[0] == '':
                return ''
            else:
                return '.' + name_elements[1]
        return ''




