import numpy as np
import xlrd
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
datamatrix=np.array(list_values)
print(datamatrix)
