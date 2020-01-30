import unittest
import types
import queue

from worker import worker, download, get_title

class TestGetter(unittest.TestCase):
    def test_get_title(self):
        url = "https://www.google.pl/"
        title = get_title(url)
        self.assertEqual("Google", title)
    def test_worker(self):
        q = queue.Queue()
        s = queue.Queue()
        q.put(None)
        worker(q,s)


if __name__ == '__main__':
    unittest.main()