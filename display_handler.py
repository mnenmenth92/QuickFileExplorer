from config import (
    colors,
    selected_background,
    default_background,
    path_color,
    type_line_color,
    path_line_num,
    folder_content_line_num,
    type_line_num
)

class DisplayHandler:
    def __init__(self, folder):
        self.folder = folder

    # retruns list of folders elements with colors and y position
    def folders_elements_format(self, selected_line, filter =''):

        interface_list = []
        folder_content = self.folder.get_content()
        line_num = 0
        for indx, folder_element in enumerate(folder_content):
            if filter in folder_element:

                if indx == selected_line:
                    background_color = selected_background
                else:
                    background_color = default_background

                extension = self.folder.element_type_string(folder_element)
                foreground_color = colors[extension]
                interface_list.append((folder_element, foreground_color, background_color, folder_content_line_num + line_num))
                line_num += 1
        return interface_list



    # return path with colors and y position
    def path_format(self):
        return (self.folder.current_path, path_color, default_background, path_line_num)

    # return type line colors and line position
    def type_format(self):
        return('', type_line_color, default_background, type_line_num)



