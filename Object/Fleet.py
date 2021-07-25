import pandas as pd;

class Fleet:
    def __init__(self, thisname, thisqty):
        self.fleetName = thisname;
        self.fleetQty = thisqty;

    def getFleetName(self):
        return self.fleetQty;

    def getFleetQty(self):
        return self.fleetQty;

    def toString(self):
        return "(" + self.fleetName + ", " + str(self.fleetQty) + ")";