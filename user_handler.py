import curses

'''
curses: https://docs.python.org/2/library/curses.html


'''


class UserHandler():

    def __init__(self, window):
        self.key = curses.KEY_UP  # variable init
        self.window = window
        self.input_string = ''


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
        pass

    # reset whole interface
    def reset_terminal(self):
        pass

    # add character to user input line
    def add_char(self):
        pass

    # remove last character from user input line
    def backspace(self):
        pass


    def curses_main_loop(self, stdscr):
        pass
