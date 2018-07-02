# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import signal
import time

# ==== CONSTANTS DEFINITIONS ==================================================
PERIOD = 5

# ==== CLASS DEFINITION =======================================================


class JoanCode():

    # _________________________________________________________________________
    def __init__(self):
        self.finished = False

    # _________________________________________________________________________
    def joan_code(self):
        print("Joan, here your code!!!")

    # _________________________________________________________________________
    def handler(self, signum, frame):
        self.finished = True
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

            # Wait for the time to finish, this can be improved by using a
            # blocking operation.
            while True:
                time.sleep(1)
                if self.finished:
                    break


if __name__ == "__main__":
    jc = JoanCode()
    jc.main()
