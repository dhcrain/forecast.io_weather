import unittest
from unittest.mock import Mock
from forecast import readable_time, temp_format


class MyTest(unittest.TestCase):
    def test_time(self):
        self.assertEqual(readable_time(1401268348), '5am')
        self.assertEqual(readable_time(0000000000), '7pm')

    def test_temp(self):
        PINK = '\033[95m'
        self.assertEqual(temp_format(PINK, 32), '\x1b[95m32°F\x1b[0m')

if __name__ == '__main__':
    unittest.main()