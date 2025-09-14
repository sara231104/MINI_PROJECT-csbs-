
import pandas as pd
df = pd.read_csv("KDDTrain+.txt", sep=",")
df.to_csv("dataset.csv", index=False)