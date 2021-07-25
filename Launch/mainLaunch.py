import numpy as np;
import pandas as pd;

from Input.DataManager import DataManager;
from Input.DataInput import DataInput;

dataInput = DataInput();
dataManager = DataManager(dataInput);

dataInput.readData();
dataManager.showInfo();

print("Finish running. ");