import curses
import importlib
import inspect
from config import type_line_num


'''
curses: https://docs.python.org/2/library/curses.html
'''

class UserHandler:

    def __init__(self, window):
        self.key = curses.KEY_UP  # variable init
        self.window = window
        self.curses = curses
        self.input_string = ''
        self.input_line = type_line_num  # to be set
        self.continue_loop = True
        self.functions_list = []
        self.selected_element = 0


        # build function list
        for name, cls in inspect.getmembers(importlib.import_module("available_functions"), inspect.isclass):
            function = cls(self)
            self.functions_list.append(function)


    # select function from function_list
    def select_action(self):
        key = self.window.getch()
        for function in self.functions_list:
            if function.check_sign(key):
                function.run(key)

    # set cursor on end of type line
    def set_cursor(self):
        self.window.addstr(type_line_num, len(self.input_string), "".encode('utf-8'))


