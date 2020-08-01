import curses
import importlib
import inspect

'''
curses: https://docs.python.org/2/library/curses.html


'''


class UserHandler:

    def __init__(self, window):
        self.key = curses.KEY_UP  # variable init
        self.window = window
        self.curses = curses
        self.input_string = ''
        self.input_line = 0  # to be set
        self.continue_loop = True
        self.functions_list = []


        # build function list
        for name, cls in inspect.getmembers(importlib.import_module("available_functions"), inspect.isclass):
            function = cls(self)
            self.functions_list.append(function)

    # update specific line
    def update_line(self, line_num, line_string):
        self.window.addstr(line_num, 0, '')
        self.window.clrtoeol()
        self.window.addstr(line_num, 0, line_string)

    # change line color and background
    def set_colors(self):
        pass

    # select function from function_list
    def select_action(self):
        key = self.window.getch()
        for function in self.functions_list:
            if function.check_sign(key):
                function.run(key)

    # reset whole interface
    def reset_terminal(self):
        pass
