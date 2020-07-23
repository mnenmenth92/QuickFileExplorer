from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import win32console
import os
from config import window_name

'''
keyboard doc: https://pythonhosted.org/pynput/keyboard.html#monitoring-the-keyboard
current window: https://stackoverflow.com/questions/24072790/detect-key-press-in-python/32386410v


'''
# keyboard events handling
class KeyboardHandler:

    # class initialization
    def __init__(self):
        self.window_name = window_name
        self.current_input_string = ''
        # set consloe window name
        win32console.SetConsoleTitle(self.window_name)

    # build typed string
    def build_string(self, key):
        # add character
        try:
            if key.char:
                self.current_input_string += key.char
        except:
            # other actions/ chars
            # ToDo make check all functions in for loop
            if key == Key.backspace:
                self.current_input_string = self.current_input_string[:-1]
            if key == Key.space:
                self.current_input_string += ' '

    # reset typed string
    def reset_string(self):
        self.current_input_string = ''

    # check if desired window active
    def on_window(self):
        return self.window_name == GetWindowText(GetForegroundWindow())

    # on key press event
    def on_press_event(self, key):
        if self.on_window():
            self.build_string(key)
            self.print_string()
            if key == Key.esc:
                # Stop listener
                return False

    # temporary for tests only
    def clear_and_print_string(self):
        os.system('cls')
        print(self.current_input_string)

    # on key release event
    def on_release(self, key):
        pass


    # start keyboard event listener
    def start_keyboard_listener(self):
        with Listener(
                on_press=self.on_press_event,
                on_release=self.on_release) as listener:
            listener.join()