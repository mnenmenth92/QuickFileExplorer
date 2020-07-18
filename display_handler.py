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

    # retruns interface string
    def interface_stirngs(self, first_line, selected_line):
        formated_link = link_format + self.folder.current_path
        empty_line =  reset_format + ''
        interface_list = [formated_link, empty_line, first_line]
        folder_content = self.folder.get_content()
        for indx, folder_element in enumerate(folder_content):
            element_string = colors[folder_content[folder_element]] + folder_element
            if indx == selected_line:
                element_string = selected_background + element_string
            else:
                element_string = reset_background + element_string
            interface_list.append(element_string)
        return  interface_list

    # print interface
    def print_interface(self, first_line, selected_line):
        for line in self.interface_stirngs(first_line, selected_line):
            print(line)




