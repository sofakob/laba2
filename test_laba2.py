import unittest
from unittest.mock import patch
import io
import sys
from laba2 import laba2val

class TestPasswordValidator(unittest.TestCase):
    def test_invalid (self):
        test_input = "Pakmmklmmovgo542"
        expected_output = "You are smart person\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            laba2val(test_input)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_corotci (self):
        test_input = "Jle4"
        expected_output = "Password must have more than 10 symbols\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            laba2val(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_chistlnet (self):
        test_input = "Hkjrnfjnkjn"
        expected_output = "Password must have at least one digit\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            laba2val(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_bucvinete (self):
        test_input = "njend62jkbkjle"
        expected_output = "Password must have at least one uppercase or lowercase letter\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            laba2val(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_bucvimalenci (self):
        test_input = "JNKNKJNL266"
        expected_output = "Password must have at least one uppercase or lowercase letter\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            laba2val(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)
    
    def test_pravilno (self):
        test_input = "KJNKLN45ewkd"
        with patch('builtins.input', return_value=test_input):
            exit_code = laba2val(test_input)
            self.assertEqual(exit_code, 0)

    def test_corotciinshiy (self):
        test_input = "Short1"
        with patch('builtins.input', return_value=test_input):
            exit_code = laba2val(test_input)
            self.assertEqual(exit_code, 1)

    def test_pravcifr (self):
        test_input = "NoDigitPassword"
        with patch('builtins.input', return_value=test_input):
            exit_code = laba2val(test_input)
            self.assertEqual(exit_code, 1)

    def test_mnogobol (self):
        test_input = "nopassword123"
        with patch('builtins.input', return_value=test_input):
            exit_code = laba2val(test_input)
            self.assertEqual(exit_code, 1)

    def test_manuni(self):
        test_input = "NOPASSWORD123"
        with patch('builtins.input', return_value=test_input):
            exit_code = laba2val(test_input)
            self.assertEqual(exit_code, 1)

if __name__ == '__main__':
    unittest.main()
