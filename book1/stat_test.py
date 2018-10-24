import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
dat = sm.datasets.get_rdataset("Guerry", "HistData").data

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print(results.summary())

#
# import pandas as pd # 读取数据到DataFrame
# import urllib # 获取网络数据
# import shutil # 文件操作
# import zipfile # 压缩解压
# import os
#
# # 建立临时目录
# try:
#     os.system('mkdir bike_data')
# except:
#     os.system('rm -rf bike_data; mkdir bike_data')
#
# data_source = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip' # 网络数据地址
# zipname = 'bike_data/Bike-Sharing-Dataset.zip' # 拼接文件和路径
# urllib.request.urlretrieve(data_source, zipname) # 获得数据
#
# zip_ref = zipfile.ZipFile(zipname, 'r') # 创建一个ZipFile对象处理压缩文件
# #zip_ref.extractall(temp_dir) # 解压
# zip_ref.extractall('bike_data')
# zip_ref.close()
#
# daily_path = 'bike_data/day.csv'
# daily_data = pd.read_csv(daily_path) # 读取csv文件
# daily_data['dteday'] = pd.to_datetime(daily_data['dteday']) # 把字符串数据传换成日期数据
# drop_list = ['instant', 'season', 'yr', 'mnth', 'holiday', 'workingday', 'weathersit', 'atemp', 'hum'] # 不关注的列
# daily_data.drop(drop_list, inplace = True, axis = 1) # inplace=true在对象上直接操作
#
# daily_data.head() # 看一看数据~
#
#
# import statsmodels.api as sm # 最小二乘
# from statsmodels.stats.outliers_influence import summary_table # 获得汇总信息
# x = sm.add_constant(daily_data['temp']) # 线性回归增加常数项 y=kx+b
# y = daily_data['cnt']
# regr = sm.OLS(y, x) # 普通最小二乘模型，ordinary least square model
# res = regr.fit()    #res.model.endog
# # 从模型获得拟合数据
# st, data, ss2 = summary_table(res, alpha=0.05) # 置信水平alpha=5%，st数据汇总，data数据详情，ss2数据列名
# fitted_values = data[:,2]  #等价于res.fittedvalues