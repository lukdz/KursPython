import queue
import threading
from worker import worker


class Getter:
    """
    **Download threads menager**
    This menages threads for asynchronic content downloading 
    """
    def __init__(self):
        """
        **Create download threads**
        This cretes threads for asynchronic content downloading 
        """
        # number of worker threads to complete the processing
        self.num_worker_threads = 3

        self.q = queue.Queue()
        self.s = queue.Queue()
        self.threads = []
        for i in range(self.num_worker_threads):
            t = threading.Thread(target=worker, args=(self.q,self.s),name=str(i))
            t.start()
            self.threads.append(t)
    def put(self, item):
        """
        **Put new item for download threads**
        This provides new request for download threads 
        """
        self.q.put(item)
    def close(self):
        """
        **Close download threads**
        This sends close request to download threads 
        """
        # block until all tasks are done
        self.q.join()

        # stop workers
        for i in range(self.num_worker_threads):
            self.q.put(None)
        for t in self.threads:
            t.join()
    def get(self):
        """
        **Get status bask from download threads**
        This retrives status updates from download threads 
        """
        try:
            return self.s.get_nowait()
        except queue.Empty:
            pass
            # print("No updates")

if __name__ == "__main__":
    g = Getter()
    g.put('Test 1')