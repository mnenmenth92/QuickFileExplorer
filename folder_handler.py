import os

# folder handling
class FolderHandler:
    def __init__(self, default_path):
        self.current_path = default_path

    # list current folder
    def get_content(self):
        return os.listdir(self.current_path)