
import sys
import signal

def graceful_shutdown(signum, frame):
    print("\nS.C.O.U.T : Have a Great Day, Goodbye!")
    sys.exit(0)
