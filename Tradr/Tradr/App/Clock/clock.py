import datetime
import sys
import signal
import os
import time


class Clock:
    @staticmethod
    def market_eod(hr, minute):
        while True:
            d = datetime.datetime.now()
            if d.hour >= hr and d.minute >= minute:
                print("The market is closed, ending the program")
                os.kill(os.getppid(), signal.SIGTERM)
                sys.exit()
            else:
                time.sleep(5)

    @staticmethod
    def clock():
        pass
