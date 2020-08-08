import os

class OneFunction(object):
    """
    All functions parent

    """

    def __init__(self, user_handler):
        self.user_handler = user_handler
        self.functions_int = -1

    # check if this is selected function by checking the functions_int
    def check_sign(self, functions_int):
        return self.functions_int == functions_int

    # run function placeholder
    def run(self, functions_int):
        pass


class Backspace(OneFunction):
    """
    removes last sign from typed line
    assigned sign: Backspace, key int value = 8
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 8

    # run function
    def run(self, functions_int):
        self.user_handler.input_string = self.user_handler.input_string[:-1]
        # remove last letter
        self.user_handler.window.addstr(self.user_handler.input_line, len(self.user_handler.input_string),
                                        " ".encode('utf-8'))
        # move cursor
        self.user_handler.window.addstr(self.user_handler.input_line, len(self.user_handler.input_string),
                                        "".encode('utf-8'))
        # filter and print content
        self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                       self.user_handler.input_string)


class Character(OneFunction):
    """
    adds character to the end of the input_string
    any character between ascii 32 and 126
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)

    # check if sign applies to this function
    def check_sign(self, functions_int):
        return functions_int < 127 and functions_int > 31

    # run function
    def run(self, functions_int):
        # add character
        self.user_handler.input_string += chr(functions_int)
        # print character
        self.user_handler.window.addstr(self.user_handler.input_line, len(self.user_handler.input_string) - 1,
                                        chr(functions_int))
        # select first item
        self.user_handler.selected_element = 0
        # filter and print content
        self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                       self.user_handler.input_string)


class Up(OneFunction):
    """
    selects upper folder element
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 259

    # run function
    def run(self, functions_int):
        if self.user_handler.selected_element > 0:
            self.user_handler.selected_element -= 1

        # filter and print content
        self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                       self.user_handler.input_string)


class Down(OneFunction):
    """
    selects lower folder element
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 258

    # run function
    def run(self, functions_int):
        # if it is not last element
        if self.user_handler.selected_element < len(self.user_handler.display.filtered_folder_content) - 1:
            # move selected element to next one
            self.user_handler.selected_element += 1
        # filter and print content
        self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                       self.user_handler.input_string)


class Right(OneFunction):
    """
    opens folder
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 261

    # run function
    def run(self, functions_int):
        # build path
        element_is_folder = self.user_handler.folder.build_path(self.user_handler.display.selected_element_string)
        if element_is_folder:
            # clear filtering input
            self.user_handler.clear_input_string()
            # update path line
            self.user_handler.display.print_path_line()
            # store current selected element
            self.user_handler.store_selected_element()
            # set selected line to the top
            self.user_handler.selected_element = 0
            # filter and print content
            self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                           self.user_handler.input_string)


class Left(OneFunction):
    """
    goes to upper folder
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 260

    # run function
    def run(self, functions_int):
        # store last path
        last_path = self.user_handler.folder.current_path
        # strip path
        self.user_handler.folder.strip_path()
        # if new path differ from previous
        if self.user_handler.folder.current_path != last_path:
            # clear filtering input
            self.user_handler.clear_input_string()
            # clear error line
            self.user_handler.display.clear_error()
            # update path line
            self.user_handler.display.print_path_line()
            # get selected element from history list
            selected_element = self.user_handler.remove_selected_element()
            # set selected element
            self.user_handler.selected_element = selected_element
            # filter and print content
            self.user_handler.display.print_folder_content(self.user_handler.selected_element,
                                                           self.user_handler.input_string)


class OpenExplorer(OneFunction):
    """
    opens current path in explorer
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 4

    def run(self, functions_int):
        # open current path in file explorer
        path = os.path.realpath(self.user_handler.folder.current_path)
        os.startfile(path)


class Enter(OneFunction):
    """
    opens selected folder in explorer
    open files in windows default app
    runs file
    """

    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_ints_list = [10, 459]

    def check_sign(self, functions_int):
        return functions_int in self.functions_ints_list

    def run(self, functions_int):
        # open current path in file explorer
        path = os.path.realpath(self.user_handler.folder.join_path(self.user_handler.display.selected_element_string))
        os.startfile(path)


# Temporary

class CtrlC(OneFunction):
    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 3

    def run(self, func_num):
        self.user_handler.continue_loop = False
