import curses
from config import (
    colors,
    selected_background,
    default_background,
    path_color,
    type_line_color,
    path_line_num,
    folder_content_line_num,
    type_line_num,
    last_selected_element
)

class DisplayHandler:
    def __init__(self, folder, window):
        self.folder = folder
        self.window = window
        self.curses = curses
        self.filtered_folder_content =[]
        self.selected_element_string = ''

    # retruns list of folders elements with colors and y position
    def folders_elements_format(self, selected_line, filter =''):
        """
        list folder with color formatting
        sets different format for selected line

        :param selected_line: int, selected line number - first folder element = 0
        :param filter: string - listed only elements which contains this string. If empty all listed.
        :return: list of tuples: (line content, foreground color, bacground color, line number)
        """

        interface_list = []
        folder_content = self.folder.get_content()
        line_num = 0
        for indx, folder_element in enumerate(folder_content):
            if filter in folder_element:

                if indx == selected_line:
                    background_color = selected_background
                    self.selected_element_string = folder_element
                else:
                    background_color = default_background

                extension = self.folder.element_type_string(folder_element)
                try:
                    foreground_color = colors[extension]
                except:
                    foreground_color = colors['default']
                interface_list.append((folder_element, foreground_color, background_color, folder_content_line_num + line_num))
                line_num += 1
        return interface_list

    # return path with colors and y position
    def path_format(self):
        return (self.folder.current_path, path_color, default_background, path_line_num)

    # return type line colors and line position
    def type_format(self):
        return ('', type_line_color, default_background, type_line_num)

    # clear selected line
    def clear_line(self, line):
        self.curses.setsyx(line, 0)
        self.window.clrtoeol()


    # update specific line
    def update_line(self, print_tuple, start_line = 0):
        # init and set color pair
        # every line has its color pair
        pair_number = print_tuple[3] + 1  # can't be zero
        self.curses.init_pair(pair_number, print_tuple[1], print_tuple[2])
        self.window.attron(self.curses.color_pair(pair_number))
        # print string ToDo check the reason
        try:
            self.window.addstr(print_tuple[3] - start_line, 0, print_tuple[0])
        except curses.error:
            print("there was an error in {}".format(print_tuple[0]))

    # check window size, returns number of rows
    def get_window_size(self):
        rows, columns = self.window.getmaxyx()
        return rows

    # set the position of first content element according to current position and content length
    def get_start_position(self,  selected_line, content=[]):
        window_size = self.get_window_size()
        needed_content_length = folder_content_line_num + selected_line + last_selected_element
        if len(content) + folder_content_line_num > window_size:
            if needed_content_length > window_size:
                return needed_content_length - window_size
        return 0

    # print path line
    def print_path_line(self):
        self.clear_line(path_line_num)
        self.update_line(self.path_format())

    # clear content
    def clear_printed_content(self):
        content_length = len(self.filtered_folder_content)
        for line_number in range(content_length):
            self.clear_line(folder_content_line_num + line_number)


    # print folder content
    def print_folder_content(self, selected_line, filter=''):
        self.window.clrtobot()
        self.filtered_folder_content = []
        content = self.folders_elements_format(selected_line, filter)
        start_line = self.get_start_position(selected_line, content)
        for index, element in enumerate(content):
            if index >= start_line:
                self.update_line(element, start_line)
            self.filtered_folder_content.append(element[0])
        # set type format after printing
        self.curses.init_pair(type_line_num + 1, self.type_format()[1], self.type_format()[2])
        self.window.attron(self.curses.color_pair(type_line_num + 1))









