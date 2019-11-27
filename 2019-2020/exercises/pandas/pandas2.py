import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/anuzzolese/genomics-unibo/master/2019-2020/data/Auto.csv", delimiter=",")

print(df.shape)
print(df.head())
print(df.describe())

s_1 = df.loc[:, ['mpg', 'cylinders', 'origin', 'name']]
s_2 = df.iloc[:, [0, 1, 4, 8]]
print(s_1)
print(s_2)
print(df.index)
print(df.columns)

m = df.loc[:, 'weight'].mean()
print("Mean weight: " + str(m))

df_w_sort = df.sort_values(by=['weight', 'cylinders'], ascending=False)
print(df_w_sort.loc[:, ['weight', 'cylinders', 'name']])
print(df.loc[54, ['weight', 'name']])

df_i_sort = df.sort_index(axis=1, ascending=False)
df_i_sort.rename(columns={'name': 'number of cars'})

df_2 = df.groupby('cylinders', as_index=False).count()
df_2.rename(columns={'name': 'number of cars'}, inplace=True)
cars_df = df_2.loc[:,["cylinders", "number of cars"]].sort_values(by="number of cars", ascending=False)
#c_df = cars_df.reindex(np.linspace(0, cars_df.shape[0]+1, cars_df.shape[0], 1))
print(cars_df.reset_index().loc[:, ["cylinders", "number of cars"]])