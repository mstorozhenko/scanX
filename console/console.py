import sys
import time


def animated_indicator(stop_event):
    while not stop_event.is_set():
        for indicator in '|/-\\':
            sys.stdout.write(f'\rWorking... {indicator}')
            sys.stdout.flush()
            time.sleep(0.1)
