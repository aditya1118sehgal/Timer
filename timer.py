import time
import pandas as pd
from tabulate import tabulate

class TimerError(Exception):
        """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start the timer"""
        if self._start_time is not None:
            raise TimerError ('Timer is running.... stop using .stop()')

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer and summarize elapsed time"""
        if self._start_time is None:
            raise TimerError ('Timer stopped, use .start() to start again')

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        print (tabulate (pd.DataFrame ({
            'seconds': [elapsed_time],
            'minutes': [elapsed_time / 60],
            'hours': [elapsed_time / 3600]
        }), showindex = False, headers = 'keys', tablefmt = 'psql'))

def main (sleep_time_secs = 1):
    t = Timer ()
    t.start ()
    time.sleep (sleep_time_secs)
    t.stop ()

if __name__ == '__main__':
    main ()
