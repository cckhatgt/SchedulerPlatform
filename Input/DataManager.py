
class DataManager:
    def __init__(self, datainput):
        self.fleetList = datainput.fleetList;

    def showInfo(self):
        print("Number of fleets = ", len(self.fleetList));

        # index = 0;
        # for record in self.fleetList:
        #     print(index, record.toString())
        #     index += 1;

        for index, record in enumerate(self.fleetList):
            print(index, ")", record.toString())