from config import (
    colors,
    selected_background,
    default_background
)

class DisplayHandler:
    def __init__(self, folder):
        self.folder = folder

    # retruns list of interface lines
    def interface_strings(self, first_line_num, selected_line, filter =''):

        interface_list = []
        folder_content = self.folder.get_content()
        for indx, folder_element in enumerate(folder_content):
            if filter in folder_element:
                if indx == selected_line:
                    background_color = selected_background
                else:
                    background_color = default_background

                extension = self.folder.element_type_string(folder_element)
                foreground_color = colors[extension]
                interface_list.append((folder_element, foreground_color, background_color))

        return interface_list

    # print interface
    def print_interface(self, first_line, selected_line):
        for line in self.interface_strings(first_line, selected_line):
            print(line)


