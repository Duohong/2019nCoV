from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

mpl.rcParams['font.family']="SimHei"
mpl.rcParams['axes.unicode_minus']=False # in case minus sign is shown as box

dfData = pd.read_csv('data.csv')
dfChina = dfData[dfData['Region']=='China']

nChina = len(dfChina)

#NewCases
plt.figure(1)
newConfirmed, = plt.plot(dfChina['Date'], dfChina['NewConfirmed1'], '-', linewidth=2, c='y')
newSevere, = plt.plot(dfChina['Date'], dfChina['NewSevere2'], '-', linewidth=2, c='r')
newDeaths, = plt.plot(dfChina['Date'], dfChina['NewDeaths3'], '-', linewidth=2, c='black')
newReleased, = plt.plot(dfChina['Date'], dfChina['NewReleased4'], '-', linewidth=2, c='g')
newSuspected, = plt.plot(dfChina['Date'], dfChina['NewSuspected5'], '-', linewidth=2, c='b')
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], 0, 5500))
plt.xticks(dfChina['Date'], dfChina['Date'])
plt.xlabel('Date 日期')
plt.title('2019nCoV China NewCases 全国 新增')
plt.grid(True)
plt.legend([newSuspected, newConfirmed, newSevere, newReleased, newDeaths], [u'New Suspected 新增疑似', u'New Confirmed 新增确诊', u'New Severe 新增重症', u'New Released 新增治愈', u'New Deaths 新增死亡'])
plt.savefig('NewCases.png')

plt.show()