import queue
import threading
from worker import worker


class Getter:
    def __init__(self):
        # number of worker threads to complete the processing
        self.num_worker_threads = 3

        self.q = queue.Queue()
        self.s = queue.Queue()
        self.threads = []
        for i in range(self.num_worker_threads):
            t = threading.Thread(target=worker, args=(self.q,self.s))
            t.start()
            self.threads.append(t)
    def put(self, item):
        self.q.put(item)
    def close(self):
        # block until all tasks are done
        self.q.join()

        # stop workers
        for i in range(self.num_worker_threads):
            self.q.put(None)
        for t in self.threads:
            t.join()
    def get(self):
        try:
            return self.s.get_nowait()
        except queue.Empty:
            pass
            # print("No updates")

if __name__ == "__main__":
    g = Getter()
    g.put('Test 1')