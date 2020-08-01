from folder_handler import FolderHandler
from config import (
    colors,
    selected_background,
    reset_background,
    link_format,
    reset_format)

class DisplayHandler:
    def __init__(self, folder):
        self.folder = folder

    # retruns list of interface lines
    def interface_strings(self, first_line, selected_line, filter =''):
        formated_link = self.folder.current_path
        empty_line = ''
        interface_list = [formated_link, empty_line, first_line]
        # ToDo interface_format_list = [link colors,empty line colors, line colors]
        folder_content = self.folder.get_content()
        for indx, folder_element in enumerate(folder_content):
            if filter in folder_element:
                if indx == selected_line:
                    # ToDo selected color pair number
                    pass
                else:
                    # ToDo regular color pair number
                    pass

                interface_list.append(element_string)
                # ToDo interface_format_list.append(string_colors)
        return interface_list  # ToDo return also list of formats

    # print interface
    def print_interface(self, first_line, selected_line):
        for line in self.interface_strings(first_line, selected_line):
            print(line)


