import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))

print(df.shape)
print("Number of rows: " + str(df.shape[0]))
print(df.head(df.shape[0]))

df_mean = df.mean() # Mean column per column
print("-------")
print(df_mean)
print(type(df_mean))

df_max = df.max() # Max value in each column
print("-------")
print("Max values: " + str(df_max))

df_min = df.min() # Min value in each column
print("-------")
print("Min values: " + str(df_min))

df_sum_columns = df.sum(axis=0) # Sum of the values in each column
print("-------")
print("Sum of column values: " + str(df_sum_columns))

df_sum_rows = df.sum(axis=1) # Sum of the values in each column
print("-------")
print("Sum of row values: " + str(df_sum_rows))

df_count_cols = df.count(axis=0) # Count for each column or row.
df_count_rows = df.count(axis=1)
print("-------")
print("Count of cols: " + str(df_count_cols))
print("Count of rows: " + str(df_count_rows))


df_diff = df.diff() # First discrete difference of elements
print("-------")
print("Diff: " + str(df_diff))

# standard correlation coefficient. 
# Other possibile methods are: kendall and spearman
df_corr_pears_cols = df.corr(method='pearson')
df_corr_spear_cols = df.corr(method='spearman')
df_corr_ken_cols = df.corr(method='kendall')

print("----\nPearson correlation on columns: \n", str(df_corr_pears_cols))
print("----\nSpearman correlation on columns: \n", str(df_corr_spear_cols))
print("----\nKendall correlation on columns: \n", str(df_corr_ken_cols))
