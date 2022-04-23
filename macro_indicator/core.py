import datetime

import matplotlib.pyplot as plt
import pandas
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def draw(filename,xlabel,ylabel,title):


    #读Excel文件数据
    data = pandas.read_excel(filename,names=['date','metric'], skiprows = [0,2])
    end_date = datetime.datetime(2005, 4, 8, 0, 0, 0)
    index = data[data.date == end_date].index.tolist()
    # print(data)
    x=data['date'][:index[0]+1]
    y=data['metric'][:index[0]+1]
    # print(x)
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
def dataframe2dict(dateframe):
    dict={}
    for k,v in dateframe.iterrows():
        dict[v['date']]=v['利率']
    return dict
#沪深300指数
draw(r'C:\Eastmoney\Choice\user\login\7848376428397730\MacroIndustry\中国宏观数据库-沪深300.xlsx','时间','指数','沪深300指数')
draw(r'C:\Eastmoney\Choice\user\login\7848376428397730\MacroIndustry\中国宏观数据库-沪深300TTM.xlsx','时间','指数','沪深300市盈率')
#证券化率
draw(r'C:\Eastmoney\Choice\user\login\7848376428397730\MacroIndustry\中国宏观数据库-证券化率.xlsx','时间','证券化率(%)','中国证券化率')
#股债收益率
csi300 = pandas.read_excel(r'C:\Eastmoney\Choice\user\login\7848376428397730\MacroIndustry\中国宏观数据库-沪深300TTM.xlsx', names=['date', 'PETTM'], skiprows=[0, 2])
end_date=datetime.datetime(2005,4,8,0,0,0)
indexs=csi300[csi300.date==end_date].index.tolist()
csi300=csi300.iloc[:indexs[0]+1]
print(csi300)
stock_bond_yield_pd = pandas.read_excel(r'C:\Eastmoney\Choice\user\login\7848376428397730\MacroIndustry\利率走势分析.xlsx', names=['date', '利率'], skiprows=[0, 2])
indexs=stock_bond_yield_pd[stock_bond_yield_pd.date==end_date].index.tolist()
# print(index)
stock_bond_yield_pd=stock_bond_yield_pd.iloc[:indexs[0]+1]
print(stock_bond_yield_pd)
dict = dataframe2dict(stock_bond_yield_pd)
# print(dict)
# print(dict)
# stock_bond_yield_pd_dict = dict(stock_bond_yield_pd)
# print(stock_bond_yield_pd_dict)
y=[]
x=[]
for k,csi in csi300.iterrows():
    # print(csi)
    x.append(csi['date'])
    y.append(1/csi['PETTM']-0.01*dict[csi['date']])
    # print(csi)
plt.plot(x,y)
plt.title('股债收益差')
plt.show()
# 二维数组转字典
filename=r'C:\Users\14552\Desktop\investment\市场整体估值.xls'
column_names = ['date']
for market in ['a','sh','sz','300','gem']:
    for type in ['LYR','TTM','PB','Value']:
        column_names.append(market+type)
# print(column_names)
pd = pandas.read_excel(filename, names=column_names,skiprows=[0,1])
# print(pd.columns.values)
# pd=pd[['date','300PB']]
end_date = datetime.datetime(2005, 4, 8, 0, 0, 0)
indexs = pd[pd.date == end_date].index.tolist()
pd=pd.iloc[:indexs[0]+1]
plt.plot(pd[['date']],pd[['300PB']])
plt.title('沪深300PB')
plt.show()