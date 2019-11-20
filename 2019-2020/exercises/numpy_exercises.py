import numpy as np

class OneDimensionalArray:
    def __init__(self, array):
        self.array=array
        print("Input array:", array)
        
    def odd_indexes(self):
        new=self.array[1::2]
        return new
        
    def back(self):
        backwards=self.array[::-1]
        return backwards
       

class TwoDimensionalArray:
	def __init__(self, array):
		self.array = array
		print ("Input matrix:", array)
	
	def reverse_columns (self):
		r = self.array [:, ::-1]
		return r
	
	def reverse_rows (self):
		b = self.array [ ::-1, : ]
		return b
		
	def reverse_columns_rows (self) :
		ba = self.array [::-1, ::-1]
		return ba 
	
	def cut (self) :
		c = self.array [1:-1, 1:-1]
		return c

# Point 1 of the exercise that instantiates a one-dimensional NumPy array.
v=np.array([11, 12, 13, 14, 15])
oda = OneDimensionalArray(v)

odds = oda.odd_indexes()
backwards = oda.back()

print("Point 1")
print("Values in odd indexes:", odds)
print("Array in backword ordering:", backwards)

print("----------------------------")

# Point 2 of the exercise that instantiates a two-dimensional NumPy array.
m = np.array([
 [11, 12, 13, 14, 15],
 [21, 22, 23, 24, 25],
 [31, 32, 33, 34, 35],
 [41, 42, 43, 44, 45],
 [51, 52, 53, 54, 55]]) 

tda = TwoDimensionalArray(m)
rc = tda.reverse_columns()
rr = tda.reverse_rows()
rcr = tda.reverse_columns_rows()
cut = tda.cut()

print("Reverse columns:", rc)
print("Reverse rows:", rr)
print("Reverse columns and rows", rcr)
print("Cut matrix", cut)