import unittest
from available_functions import OneFunction, Backspace

class FunctionsTest:

    # test backspace function
    def test_backspace(self, input_string):
        function = Backspace()
        function.check_sign()
