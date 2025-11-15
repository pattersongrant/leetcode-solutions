import threading

class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.hydrogen_semaphore = threading.Semaphore(2)
        self.oxygen_semaphore = threading.Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_semaphore.acquire()
        self.barrier.wait()

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

        self.hydrogen_semaphore.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_semaphore.acquire()
        self.barrier.wait()


        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()

        self.oxygen_semaphore.release()