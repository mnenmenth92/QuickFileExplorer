import curses

'''
curses: https://docs.python.org/2/library/curses.html


'''


class UserHandler():

    def __init__(self, window):
        self.key = curses.KEY_UP  # variable init
        self.window = window
        self.input_string = ''
        self.input_line = 0  # to be set
        self.continue_loop = True

    # get typed character/ string
    def get_char(self):
        self.key = self.window.getch()

    # update specific line
    def update_line(self, line_num, line_string):
        self.window.addstr(line_num, 0, '')
        self.window.clrtoeol()
        self.window.addstr(line_num, 0, line_string)

    # change line color and background
    def set_colors(self):
        pass

    # recognize further action by checking typed char
    def select_action(self):
        debug_string = ''
        key = self.window.getch()
        # ToDo write down modifiers for shortcuts
        # ToDo make additional dictionary with possible functions assigned to keys/ shortcuts
        if key == 8:
            self.backspace()
            debug_string = 'backspace'
        elif key == 3:
            self.continue_loop = False
        else:
            self.add_char(key)
            debug_string = str(int(key))
        self.debug_line('character,' + debug_string)

    # reset whole interface
    def reset_terminal(self):
        pass

    def debug_line(self, string):
        self.window.addstr(1, 0, '')
        self.window.clrtoeol()
        self.window.addstr(1, 0, string)
        self.window.addstr(2, 0, '')
        self.window.clrtoeol()
        self.window.addstr(2, 0, self.input_string)

    # add character to user input line
    def add_char(self, key):
        self.input_string += chr(key)
        self.window.addstr(self.input_line,  len(self.input_string)-1, chr(key))

    # remove last character from user input line
    def backspace(self):
        self.input_string = self.input_string[:-1]
        self.window.addstr(self.input_line, len(self.input_string), " ".encode('utf-8'))

    def curses_main_loop(self):
        while self.continue_loop:
            self.select_action()
            self.window.refresh()

