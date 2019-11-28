import pandas as pd
import matplotlib.pyplot as plt

class IrisManager:
	
	def __init__(self):
		self.__df = pd.read_csv("iris.csv")
		
	def n_rows(self):
		return self.__df.shape[0]
		
	def n_columns(self):
		return self.__df.shape[1]
		
	def avg_petal_length(self):
		return self.__df.loc[:, "petal_length"].mean()
		
	def all_avgs(self):
		return self.__df.mean()
	
	def outliers(self):
		return self.__df[self.__df.petal_length > 1.5 * self.avg_petal_length()]
		
	def std(self):
		return self.__df.groupby(self.__df.species).std()
		
	def grouped_outliers(self):
		avg = self.avg_petal_length()
		for name, dataframe in self.__df.groupby(self.__df.species):
			print(name)
			print(dataframe[dataframe.petal_length>avg])
			
	def group_wise_pl(self):
		grouped = self.__df.groupby(self.__df.species, as_index=False)
		petlen_mean_by_name = grouped.mean()
		return self.__df.merge(petlen_mean_by_name, on="species")
		

im = IrisManager()
n_rows = im.n_rows()
n_cols = im.n_columns()
avg_pl = im.avg_petal_length()
all_avgs = im.all_avgs()
outliers = im.outliers()
std = im.std()
merge = im.group_wise_pl()

print("# of rows: " + str(n_rows))
print("# of cols: " + str(n_cols))
print("Petal length mean: " + str(avg_pl))
print("All avgs: " + str(all_avgs))
print("Outliers: " + str(outliers))
print("Std: " + str(std))
im.grouped_outliers()
print(merge)
