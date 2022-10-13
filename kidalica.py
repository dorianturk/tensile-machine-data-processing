#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 00:14:07 2022

@author: dorianturk
"""

import pandas as pd

df = pd.read_csv('rezultati_kidalica/mjerenje19.5.Dorian.csv', header=None)

df = df.drop(df.columns[range(0,len(df.columns),4)], axis=1)
df = df.drop(df.columns[range(2,len(df.columns),3)], axis=1)
df = df.drop(index=0)

print(df)


"""
df.to_excel("rezultati_kidalica/mjerenje19_5_Dorian.xlsx", index=False, sheet_name='mjerenje', float_format="%,2f")
"""