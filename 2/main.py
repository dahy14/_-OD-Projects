# Creating a truth table maker using numpy
import numpy as np
import pandas as pd

vInt4 = np.array(
    [[False, False, False, False], 
    [False, False, False, True],
    [False, False, True, False],
    [False, False, True, True],
    [False, True, False, False],
    [False, True, False, True],
    [False, True, True, False],
    [False, True, True, True],
    [True, False, False, False],
    [True, False, False, True],
    [True, False, True, False],
    [True, False, True, True],
    [True, True, False, False],
    [True, True, False, True],
    [True, True, True, False],
    [True, True, True, True]], 
    dtype=np.int8
)
names = [_ for _ in 'abcd']
df = pd.DataFrame( vInt4, columns=names)

def getTruth(Gate='AND', *args, **kwargs):
    df
    pass

if __name__ == '__main__':
    getTruth()









