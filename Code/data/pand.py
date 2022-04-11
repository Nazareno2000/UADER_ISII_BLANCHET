import pandas as pd
df = pd.read_csv("Desktop\Code\data\dataset.csv",index_col="id")
print(df)
print(df.describe())
print((df.head))
print((df.tail))