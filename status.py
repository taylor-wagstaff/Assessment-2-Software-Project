from colors import bcolors

class status:
    OPEN = bcolors.OKGREEN + "OPEN" + bcolors.ENDC
    SUBMITTED = bcolors.OKYELLOW + "SUBMITTED" + bcolors.ENDC
    CLOSED = bcolors.OKRED + "CLOSED" + bcolors.ENDC