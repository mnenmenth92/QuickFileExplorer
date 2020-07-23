import unittest
from keyboard_handler import KeyboardHandler



class KeyboardHandlerTest(unittest.TestCase):

    # set up tests
    def setUp(self):
        self.keyboard = KeyboardHandler()

    # build string that is be used in further tests
    def build_default_string(self):
        self.keyboard.build_string('a')
        self.keyboard.build_string('b')
        self.keyboard.build_string('c')

    #check reset string
    def test_reset_string(self):
        self.build_default_string()
        self.keyboard.reset_string()
        self.assertEqual(self.keyboard.current_input_string, '')

    # check character add
    def test_build_string_add(self):
        self.build_default_string()
        self.assertEqual(self.keyboard.current_input_string, 'abc')

    # check character remove
    def test_build_string_remove(self):
        self.build_default_string()
        self.keyboard.build_string('Key.backspace')
        self.assertEqual(self.keyboard.current_input_string, 'ab')






if __name__ == '__main__':
    unittest.main()



