

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
        self.user_handler.input_string += chr(functions_int)
        self.user_handler.window.addstr(self.user_handler.input_line, len(self.user_handler.input_string)-1,
                                        chr(functions_int))


# Temporary
class CtrlC(OneFunction):
    def __init__(self, user_handler):
        super().__init__(user_handler)
        self.functions_int = 3
    def run(self, func_num):
        self.user_handler.continue_loop =False


