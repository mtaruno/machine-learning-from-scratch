import unittest
import sys
from pathlib import Path
if __package__ is None:                  
    DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name
import fundementals.data_manipulation as dm
import numpy as np
import numpy as np


class TestDataManipulation(unittest.TestCase):
    def test_shuffle(self):
        x = np.arange(5,10)
        y = np.arange(5)
        x, y = dm.shuffle_data(x,y,seed=33)
        print(x)
        print(y)

    def test_train_test_split(self):
        X = pd.DataFrame()
        y = 
        

unittest.main()
