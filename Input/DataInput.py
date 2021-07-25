
import pandas as np;

from Object.Fleet import Fleet;

class DataInput:
    def __init__(self):
        self.fleetList = [];

    def readData(self):
        self.readFleet("..\\data\\fleets.csv");
        return;

    def readFleet(self, filename):
        file = np.read_csv(filename, header=None).values;

        for record in file:
            newfleet = Fleet(record[0], record[1]);
            self.fleetList.append(newfleet);

        return;