
import pandas as pd
df = pd.read_csv("KDDTrain+.txt", sep=",")
df.to_csv("dataset1.csv", index=False)
df = pd.read_csv("KDDTest+.txt", sep=",")
df.to_csv("testdataset.csv", index=False)