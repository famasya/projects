import sys
import time

import daemonocle

# This is your daemon. It sleeps, and then sleeps again.
def main():
    while True:
        time.sleep(10)

if __name__ == '__main__':
    daemon = daemonocle.Daemon(
        worker=main,
        pidfile='/var/run/daemonocle_example.pid',
    )
    daemon.do_action(sys.argv[1])
