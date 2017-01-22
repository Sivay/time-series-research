import pandas as pd
import numpy as np

from method.DPXA import MF_DPXA
from method.DCCA import MF_DCCA

point = 200
A = DPXA(-5, 5, 1, 'period1_1.csv')
index = A.flist.index(2.0)
A.generate()
print(A.hurst_list[index])
B = DPXA(-5, 5, 1, 'period1_2.csv')
B.generate()
C = DPXA(-5, 5, 1, 'period1_3.csv')
C.generate()
#df.iloc[np.random.permutation(len(df))]