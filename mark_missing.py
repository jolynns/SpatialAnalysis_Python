import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/housing.csv')

col_names = list(df)
print(col_names)


for i in col_names:
    if df[i].isnull().values.any():
        new_name ="m_" + i
        df[new_name] = df.apply(lambda row: 1 if np.isnan(row[i]) else 0, axis=1)
##            dataframe.apply
##    		dataframe[i].fillna(dataframe[i].median(skipna=True), inplace = True)
    else:
        continue

print(list(df))
print(df['m_total_bedrooms'].value_counts(ascending=True))
