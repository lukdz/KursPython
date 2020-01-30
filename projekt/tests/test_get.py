import unittest
import types

import context
from get import Getter

class TestGetter(unittest.TestCase):
    def testProsty(self):
        getter = Getter()
        url = "https://www.google.pl/"
        getter.put((1,url))
        result = getter.get()
        while result is None:
            result = getter.get()
        self.assertEqual("(1, 'Downloading')", str(result))
        result = getter.get()
        while result is None:
            result = getter.get()
        self.assertEqual("(1, 'Downloaded')", str(result))
        getter.close()

if __name__ == '__main__':
    unittest.main()