import csv
import pandas
#from datetime import datetime

df = pandas.read_csv('Trade History 2021-08-30.csv', sep=None, header=0, engine='python', parse_dates=[0], infer_datetime_format=True)
df.to_csv('Td-modified.csv', index = False, quoting=csv.QUOTE_NONE, escapechar='\\', date_format='%Y/%m/%d %HH:%MM:%S' )
print(df.iloc[:,0])
