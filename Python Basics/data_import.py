#IMPORTING DATA
#data imported in spyder is dataframes
#Tabular rows--sample  coloumn--variable
import pandas as pd

csv1=pd.read_csv('csv_eg.csv',index_col=0)
print(csv1)

xls1=pd.read_excel('xls_eg.xls',index_col=0)
print(xls1)

txt1=pd.read_table('dna.txt',na_values=['??'], delimiter=" ")
print(txt1)                                                    