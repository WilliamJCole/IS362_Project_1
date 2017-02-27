# -*- coding: utf-8 -*-
'''Flight Delays'''

import pandas as pd
import numpy as np
import os

Location = open(os.path.expanduser(r'~/IS362_Spring_2017/Project_1/delays.csv'))

df = pd.read_csv(Location)

print df.head()

sumofrows = data.set_index(['Airlines', 'Status'])
sumofrows['Total'] = sumofrows.sum(axis=1)

print(sumofrows)


alaska_total = sumofrows.xs('Alaska').xs('delayed') + sumofrows.xs('Alaska').xs('on time')
amwest_total = sumofrows.xs('AM West').xs('delayed') + sumofrows.xs('AM West').xs('on time')

alaska_totaldelay = sumofrows.xs('Alaska').xs('delayed')
alaska_delay = (alaska_totaldelay/alaska_total*100).round(2)

amwest_totaldelay = sumofrows.xs('AM West').xs('delayed')
amwest_delay = (amwest_totaldelay/amwest_total*100).round(2)

print('Delays Stats: \n Alaska Airlines\n'
      ,alaska_delay[0:-1], '\n --------------- \n AM West Airlines\n'
      ,amwest_delay[0:-1], '\n --------------- \n'
      ,'Alaska Airlines flights delayed: ',alaska_delay[-1],'%\n'
      ,'AM West Airlines flights delayed: ',amwest_delay[-1],'%'
     )
