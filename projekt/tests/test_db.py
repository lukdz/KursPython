import unittest
import types

import context
from db import add_url, list_urls, update_status

class TestDB(unittest.TestCase):
    def test_add(self):
        values = list_urls()
        counter = len(values)
        add_url('_NEW_PAGE_', 'waiting')
        values = list_urls()
        self.assertEqual(counter+1, len(values))

if __name__ == '__main__':
    unittest.main()