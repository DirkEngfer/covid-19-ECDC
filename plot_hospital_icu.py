#!/usr/bin/env python
# coding: utf-8

import os, numpy as np
import pandas as pd
from matplotlib import pyplot as plt
homedir = os.getenv('HOME')

datapath = os.path.join(homedir, 'Dokumente','python-apps','tensorflow', 'covid-19', 'icu_admission_2020')
datafile = 'data.csv'

indatapath = os.path.join(datapath,datafile)

df = pd.read_csv(indatapath, header=0, sep=',',usecols=[0,1,2,4])
df = df[  (df.indicator=='Daily ICU occupancy') & ( (df.country == 'France') | (df.country == 'Germany'))  ]
df['dt'] = pd.to_datetime(df.date, format='%Y-%m-%d')
df.sort_values(by=['country', 'dt'], ascending=[True, True], inplace=True, axis=0)
df_ger = df[(df.country == 'Germany')]
df_fr  = df[( (df.country == 'France') & (df.dt >= pd.to_datetime('20200320', format='%Y%m%d')) )]

fig, ax = plt.subplots(figsize=[20,15])
ax.plot(df_ger['dt'], df_ger['value'], label='Germany', color='red')
ax.plot(df_fr['dt'], df_fr['value'], label='France', color='blue')

#ax.set_xlim(1960, 2018)
ax.tick_params(labelsize=18)

ax.set_title('ICU admission occupancy in the EU', fontsize='24')
ax.legend(loc=3, prop={'size': 18})
ax.grid(True)
t = "Copyright owner of the data published for download:\nECDC [2005-2021].\n(European Centre for Disease Prevention and Control)"
ax.text('2020-09', 6500, t, fontsize=18)

plt.xlabel('Time since 20th March, 2020', fontsize='xx-large')
plt.ylabel('Counts', fontsize='xx-large')
#fig.autofmt_xdate(rotation=30)
plt.savefig('icu_admission_occupancy.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', format='png')


