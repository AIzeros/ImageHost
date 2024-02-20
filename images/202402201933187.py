import pandas as pd

data1 = pd.read_excel("GSE108000(3) total.xlsx")
data2 = pd.read_excel("基因对应1.xlsx")

data = pd.merge(data1, data2, on="ID", how="left")
print(data.head())
data.to_excel("GSE108000(3) totalmerge.xlsx", index=None)