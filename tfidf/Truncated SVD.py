import numpy as np
import xlrd
from scipy.linalg import svd 

data = xlrd.open_workbook('C:\\Users\\SingSing\\Documents\\GitHub\\SVD-and-Truncated-SVD\\tfidf\\tfidf_result.xlsx')
table = data.sheets()[0]
# print(table)
# nrows = table.nrows 
# ncols = table.ncols 
# c1=arange(0,nrows,1)
# print(c1)

start=1  #start row
end=5  #end row
 
rows=end-start

list_values=[]
for x in range(start,end):
    values=[]
    row =table.row_values(x)
    for i in range(1,11):
        # print(value)
        values.append(row[i])
    list_values.append(values)
# print(list_values)
X=np.array(list_values)
print('\n X = \n', X) 
U, s, VT = svd(X)

print('\nU = \n', U) 
print('s = \n', s) 
print('VT = \n', VT)

k=2
recovered_X= U[:,:k].dot(np.diag(s)[:k,:k]).dot(VT [:k, :])
print("\n X_%d = \n" %k , recovered_X) 
