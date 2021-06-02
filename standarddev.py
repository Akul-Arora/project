import csv
import pandas as pd
import statistics

df=pd.read_csv("105data.csv")
listvalue=df["standarddeviation"].tolist()

meanvalue_mean=statistics.mean(listvalue)
print("mean=",meanvalue_mean)

standarddeviation=statistics.stdev(listvalue)
print("standard deviation=",standarddeviation)