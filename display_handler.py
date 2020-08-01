from config import (
    colors,
    selected_background,
    default_background,
    path_color,
    type_line_color
)

class DisplayHandler:
    def __init__(self, folder):
        self.folder = folder

    # retruns list of folders elements with colors
    def folders_elements_format(self, selected_line, filter =''):

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



    # return path with colors
    def path_format():
        return (self.folder.current_path, path_color, default_background)




