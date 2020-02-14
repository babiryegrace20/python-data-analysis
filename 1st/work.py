import pandas as pd
import csv
data = pd.read_csv('/Users/Nicholask/Desktop/countries.csv')
sa = data[data.Region == 'SOUTH AMERICA']
sa.to_csv("Desktop/sa.csv")
ss = sa.drop(["Region"],axis=1)
ss.to_csv("Desktop/South_America.csv")