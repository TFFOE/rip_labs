from time import time
from time import sleep
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start_time = time()

    def __enter__(self):
        return
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(f'time: {round(time() - self.start_time, 3)}')

@contextmanager
def cm_timer_2():
    start_time = time()
    yield
    print(f'time: {round(time() - start_time, 3)}')

with cm_timer_2():
    sleep(2.2)