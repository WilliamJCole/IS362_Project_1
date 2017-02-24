# -*- coding: utf-8 -*-
'''Flight Delays'''

import pandas as pd
import numpy as np
import os

Location = open(os.path.expanduser(r'~/IS362_Spring_2017/Project_1/delays.csv'))

df = pd.read_csv(Location)

print df.head()

stack = df.stack()
print stack
