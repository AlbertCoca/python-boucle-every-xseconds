# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import signal
from multiprocessing import Pipe

# ==== CONSTANTS DEFINITIONS ==================================================
PERIOD = 1

# ==== CLASS DEFINITION =======================================================


class JoanCode():

    # _________________________________________________________________________
    def __init__(self):
        self.finished = False

        # Get two sides of a pipe.
        self.p_left, self.p_right = Pipe()

    # _________________________________________________________________________
    def joan_code(self):
        print("Joan, here your code!!!")

    # _________________________________________________________________________
    def handler(self, signum, frame):
        self.p_left.send(1)
        # Unset signal
        signal.alarm(0)

    # _________________________________________________________________________
    def main(self):
        # Set signal handler
        signal.signal(signal.SIGALRM, self.handler)

        # Tu boucle
        while True:
            self.finished = False

            # Boucle will be executed every PERIOD
            signal.alarm(PERIOD)

            # Your code whatever it is.
            self.joan_code()

            # Block the process until the time is finished.
            self.p_right.recv()


if __name__ == "__main__":
    jc = JoanCode()
    jc.main()
