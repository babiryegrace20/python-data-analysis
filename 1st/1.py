# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:49:01 2019

@author: GRACE
"""

import pandas as pd
import csv
data = pd.read_csv('C:\Users\GRACE\Desktop\recess2\python\1st\countries.csv')
sa = data[data.Region == 'SOUTH AMERICA']
sa.to_csv("1st/sa.csv")
ss = sa.drop(["Region"],axis=1)
ss.to_csv("1st/South_America.csv")