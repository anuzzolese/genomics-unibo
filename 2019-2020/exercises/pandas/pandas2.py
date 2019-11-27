import pandas as pd

# We read the CSV.
# If the CSV is available on line, Pandas allows to read it by providing its URL as input argument.
df = pd.read_csv("https://raw.githubusercontent.com/anuzzolese/genomics-unibo/master/2019-2020/data/Auto.csv", delimiter=",")

# We compute the shape of the data frame.
# The shape is a tuple with two elements, i.e. the data frame is a bidimensional data structure. 
# The first element of the tuple (i.e. DataFrame.shape[0]) returns the number of rows of the data frame.
# Similarly, the second element of the tuple (i.e. DataFrame.shape[1]) returns the number of columns of the data frame.
# DataFrame.shape is a (public) attribute that is available for any object which is an instance of the class DataFrame.
print(df.shape)

# We print the first 5 rows on terminal.
# DataFrame.head() is the method for obtaining the first n rows.
# By default DataFrame.head() returns the first 5 rows (i.e. n=5).
# Different values for n can be requested, e.g. DataFrame.head(15) returns the first 15 rows.
print(df.head())

# The method DataFrame.describe() generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
# It Analyses both numeric and object series, as well as DataFrame column sets of mixed data types. The output will vary depending on what is provided.
# Please refer to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html for additional information.
print(df.describe())

# With the attribute DataFrame.index we get the indexes associated with each row of the data frame.
print(df.index)

# Similarly, with the attribute DataFrame.columns we get the labels associated with each column of the data frame.
print(df.columns)

# We get a slice of the data frame that includes all the rows, but only the
# columns 'mpg', 'cylinders', 'origin', and 'name'. We do that by using DataAccess.loc. 
# DataFrame.loc accesses a group of rows and columns by label(s) or a boolean array.
# More details can be found at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html.
s_1 = df.loc[:, ['mpg', 'cylinders', 'origin', 'name']]

# Then we get another slice that includes all the rows, byt only the columns associated with the indexes
# 0, 1, 4, and 8, respectively. This slicing is performed with iloc, which is a purely integer-location based indexing for selection by position.
# More details at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html.
s_2 = df.iloc[:, [0, 1, 4, 8]]

# We prrint s_1 and s_2
print(s_1)
print(s_2)

# Now we use DataFrame.loc to obtain a Series from the column 'weigth'. We then get a value that represent the arithmetic mean computed on the values representing weights.
# A Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
# On the contrary a Data Frame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
m = df.loc[:, 'weight'].mean()
print("Mean weight: " + str(m))

# We use DataFrame.sort_values in order to sort the values first by the column 'weight' then by the column 'cylinders'.
# The direction of the sorting is descending (i.e. the argument 'ascending' is set to False).
df_w_sort = df.sort_values(by=['weight', 'cylinders'], ascending=False)

# Then we print the slice of the sorted data frame by using all the rows (i.e. : in .loc[:, ...]) but only for the columns 'weight', 'cylinders', and 'name'.
print(df_w_sort.loc[:, ['weight', 'cylinders', 'name']])

# We can also sort the data frame not based on values contained in the data frame, but on its indexes.
# Again we sort the indexes that indefy the columns in a descending way.
df_i_sort = df.sort_index(axis=1, ascending=False)

# The DataFrame.groupby() method is used to split the data into groups based on some criteria. 
# Pandas objects can be split on any of their axes. The abstract definition of grouping is to provide a mapping of labels to group names.
# In the following line we split the data frame into several groups by using the values in the column 'cylinders'.
# The as_index option allows to use the group labels as indexes (i.e. as_index=True - by default) or not (i.e. as_index=False).
# Then we count the elements in each group, i.e. we have the number of cars with the specific number of cylinders that identifies the group.
df_2 = df.groupby('cylinders', as_index=False).count()

# We change the name of the column 'name' into 'number of cars'.
# This operation is performed in-place (inplace=True, by default inplace=False). This means that it does the renaming is not performed on 
# a new data frame returned as output, but it is done on the current data frame. Accordingly, the operation affects the data frame on wich 
# the method is invoked.
df_2.rename(columns={'name': 'number of cars'}, inplace=True)

#Finally, we create a slice of the data frame that with all the rows available but only the columns 'cylinders' and 'number of cars' (the new column that substitutes the previous 'name').
cars_df = df_2.loc[:,["cylinders", "number of cars"]]
print(cars_df)