# this demonstrates the use of alias to simplify usage
import numpyAndPlotPackage.pythonstuff as pystuff

def calltheotherPackage():
    "This uses a variable and calls a function in another package"
    print(pystuff.ys)
    pystuff.plotthing()