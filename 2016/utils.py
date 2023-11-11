
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[0;37;40m'
    BLACK = '\033[0;30;40m'
    RED = '\033[0;31;40m'
    GREEN = '\033[0;32;40m'
    YELLOW = '\033[0;33;40m'
    BLUE = '\033[0;34;40m'
    PURPLE = '\033[0;35;40m'
    CYAN = '\033[0;36;40m'
    WHITE = '\033[0;37;40m'
    
#	No effect	0	Black	40
#	Bold	1	Red	41
#	Underline	2	Green	42
#	Negative1	3	Yellow	43
#	Negative2	5	Blue	44
#			Purple	45
#			Cyan	46


def readInput(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            if l.lstrip() == "":
                continue
            lines.append(l.split("\n")[0])
    return lines

def readSingleLine(filename):
    with open(filename) as f:
        return f.readline().split("\n")[0]

def printArray(cm, points=None, color=bcolors.OKGREEN):
    if points is None:
        for y in range(cm.shape[1]):
            for x in range(cm.shape[0]):
                print (int(cm[x, y]), end="")
            print ("")
    else:
        for y in range(cm.shape[1]):
            for x in range(cm.shape[0]):
                if [x,y] in points:
                    print (color + str(int(cm[x, y])) + bcolors.ENDC, end="")
                else:
                    print (bcolors.GREY + str(int(cm[x, y])) + bcolors.ENDC, end="")
            print ("")

def printMap(cm):
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 0:
                print (".", end="")
            else:
                print (bcolors.BOLD+"#"+bcolors.ENDC, end="")
        print ("")
    print ("\n")
