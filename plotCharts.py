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
dfHB    = dfData[dfData['Region']=='HB']
dfChinaHB = dfChina.merge(dfHB, on=['Date'], how='inner')
dfChinaHBx = dfChinaHB[dfChinaHB['Date']>='2/01']

nChina = len(dfChina)

#Suspected
plt.figure(2)
currentQuarantine, = plt.plot(dfChina['Date'], dfChina['CurrentQuarantine14'], '-', linewidth=2, c='g')
currentSuspected, = plt.plot(dfChina['Date'], dfChina['CurrentSuspected11'], '-', linewidth=2, c='m')
newSuspected, = plt.plot(dfChina['Date'], dfChina['NewSuspected5'], '-', linewidth=2, c='r')
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], 0, dfChina['CurrentQuarantine14'][nChina-1]+2000))
plt.xticks(dfChina['Date'], dfChina['Date'])
plt.xlabel('Date 日期')
plt.title('2019nCoV China Suspected 全国 疑似')
plt.grid(True)
plt.legend([currentQuarantine, currentSuspected, newSuspected], [u'Current Quarantine 正在接受医学观察', u'Current Suspected 现有疑似', u'New Suspected 新增疑似'])
plt.savefig('Suspected.png')

#NewCases
plt.figure(3)
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

#HB vs Rest
plt.figure(4)
hbNewConfirmed, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewConfirmed1_y'], '-', linewidth=2)
restNewConfirmed, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewConfirmed1_x']-dfChinaHB['NewConfirmed1_y'], '-', linewidth=2)
hbNewSuspected, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSuspected5_y'], '-', linewidth=2)
restNewSuspected, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSuspected5_x']-dfChinaHBx['NewSuspected5_y'], '-', linewidth=2)
hbNewSevere, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSevere2_y'], '-', linewidth=2)
restNewSevere, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSevere2_x']-dfChinaHBx['NewSevere2_y'], '-', linewidth=2)
plt.axis(("2/01", dfChina['Date'][nChina-1], 0, 5200))
plt.xticks(dfChinaHB['Date'], dfChinaHB['Date'])
plt.xlabel('Date 日期')
plt.title('2019nCoV HuBei NewCases 湖北省新增确诊')
plt.grid(True)
plt.legend([hbNewSuspected, restNewSuspected, hbNewConfirmed, restNewConfirmed, hbNewSevere, restNewSevere], [u'HuBei New Suspected 湖北省新增疑似', u'Rest New Suspected 其他各省新增疑似', u'HuBei New Confirmed 湖北省新增确诊', u'Rest New Confirmed 其他各省新增确诊', u'HuBei New Severe 湖北省新增重症', u'Rest New Severe 其他各省新增重症'])
plt.savefig('HuBeiNewCases.png')

#plt.show()