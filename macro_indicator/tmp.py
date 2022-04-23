import pandas
import datetime
import matplotlib.pyplot as plt

filename=r'C:\Users\14552\Desktop\investment\市场整体估值.xls'
column_names = ['date']
for market in ['a','sh','sz','300','gem']:
    for type in ['LYR','TTM','PB','Value']:
        column_names.append(market+type)
# print(column_names)
pd = pandas.read_excel(filename, names=column_names,skiprows=[0,1])
# print(pd.columns.values)
pd=pd[['date','300PB']]
end_date = datetime.datetime(2005, 4, 8, 0, 0, 0)
indexs = pd[pd.date == end_date].index.tolist()
pd=pd.iloc[:indexs[0]+1]
