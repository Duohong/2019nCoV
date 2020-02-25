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
dfChina0205 = dfChina[dfChina['Date']>='2/05']
dfHB    = dfData[dfData['Region']=='HB']
dfChinaHB = dfChina.merge(dfHB, on=['Date'], how='inner')
dfChinaHBx = dfChinaHB[dfChinaHB['Date']>='2/01']
dfChinaHB0212 = dfChinaHB[dfChinaHB['Date']>='2/12']
dfBeijing = dfData[dfData['Region']=='Beijing']
dfFT = dfData[dfData['Region']=='FT']

nChina = len(dfChina)

#Confirmed
plt.figure(1)
confirmed, = plt.plot(dfChina['Date'], dfChina['Confirmed6'], '-', linewidth=2)
currentTreatment, = plt.plot(dfChina0205['Date'], dfChina0205['CurrentTreatment15'], '-', linewidth=2, c='y')
currentSevere, = plt.plot(dfChina['Date'], dfChina['CurrentSevere7'], '-', linewidth=2, c='r')
psc, = plt.plot(dfChina['Date'], 100000*dfChina['CurrentSevere7']/dfChina['Confirmed6'], '-', linewidth=2)
pst, = plt.plot(dfChina0205['Date'], 100000*dfChina0205['CurrentSevere7']/dfChina0205['CurrentTreatment15'], '-', linewidth=2)
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], 0, dfChina['Confirmed6'][nChina-1]+1000))
plt.xticks(dfChina['Date'][::2], dfChina['Date'][::2])
plt.xlabel('Date 日期')
plt.title('2019nCoV China Confirmed/CurrentSevere 全国 确诊/现有重症')
plt.grid(True)
plt.legend([confirmed, currentTreatment, currentSevere, psc, pst], 
           [u'Confirmed 确诊', u'Current Treatment 现有确诊', u'Current Severe 现有重症', u"Current Severe 现有重症/Confirmed 确诊 %", u"Current Severe 现有重症/Current Treatment 现有确诊 %"])
plt.savefig('CurrentSevere.png')

#Suspected
plt.figure(2)
currentQuarantine, = plt.plot(dfChina['Date'], dfChina['CurrentQuarantine14']//6, '-', linewidth=2, c='g')
currentSuspected, = plt.plot(dfChina['Date'], dfChina['CurrentSuspected11'], '-', linewidth=2, c='m')
newSuspected, = plt.plot(dfChina['Date'], dfChina['NewSuspected5'], '-', linewidth=2, c='r')
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], 0, 33000))
plt.xticks(dfChina['Date'][::2], dfChina['Date'][::2])
plt.xlabel('Date 日期')
plt.title('2019nCoV China Suspected 全国疑似')
plt.grid(True)
plt.legend([currentQuarantine, currentSuspected, newSuspected], [u'Current Quarantine 正在接受医学观察 / 6', u'Current Suspected 现有疑似', u'New Suspected 新增疑似'])
plt.savefig('Suspected.png')

#NewCases
plt.figure(3)
newWeakConfirmed, = plt.plot(dfChina['Date'], dfChina['NewWeakConfirmed16']/2, '--', linewidth=2, c='y')
newConfirmed, = plt.plot(dfChina['Date'], dfChina['NewConfirmed1']-dfChina['NewWeakConfirmed16'], '-', linewidth=2, c='y')
newSevere, = plt.plot(dfChina['Date'], dfChina['NewSevere2'], '-', linewidth=2, c='r')
newDeaths, = plt.plot(dfChina['Date'], dfChina['NewDeaths3'], '-', linewidth=2, c='black')
newDischarged, = plt.plot(dfChina['Date'], dfChina['NewDischarged4'], '-', linewidth=2, c='g')
newSuspected, = plt.plot(dfChina['Date'], dfChina['NewSuspected5'], '-', linewidth=2, c='b')
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], -1100, 6700))
plt.xticks(dfChina['Date'][::2], dfChina['Date'][::2])
plt.xlabel('Date 日期')
plt.title('2019nCoV China NewCases 全国新增')
plt.grid(True)
plt.legend([newWeakConfirmed, newSuspected, newConfirmed, newSevere, newDischarged, newDeaths], 
           [u'New Weak Confirmed 新增临床诊断 / 2', u'New Suspected 新增疑似', u'New Confirmed 新增确诊', u'New Severe 新增重症', u'New Discharged 新增治愈', u'New Deaths 新增死亡'])
plt.savefig('NewCases.png')

#CurrentCases
plt.figure(4)
currentQuarantine, = plt.plot(dfChina['Date'], dfChina['CurrentQuarantine14']//3, '-', linewidth=2, c='g')
currentSuspected, = plt.plot(dfChina['Date'], dfChina['CurrentSuspected11'], '-', linewidth=2, c='b')
currentTreatment, = plt.plot(dfChina0205['Date'], dfChina0205['CurrentTreatment15'], '-', linewidth=2, c='y')
currentSevere, = plt.plot(dfChina['Date'], dfChina['CurrentSevere7'], '-', linewidth=2, c='r')
currentSevereRatio, = plt.plot(dfChina0205['Date'], 100000*dfChina0205['CurrentSevere7']//dfChina0205['CurrentTreatment15'], '-', linewidth=2, c='c')
plt.axis((dfChina['Date'][0], dfChina['Date'][nChina-1], 0, 65000))
plt.xticks(dfChina['Date'][::2], dfChina['Date'][::2])
plt.xlabel('Date 日期')
plt.title('2019nCoV China CurrentCases 全国现有')
plt.grid(True)
plt.legend([currentQuarantine, currentTreatment, currentSuspected, currentSevere, currentSevereRatio], 
           [u'Current Quarantine 尚在医学观察 / 3', u'Current Treatment 现有确诊', u'Current Suspected 现有疑似', u'Current Severe 现有重症', u'Current Severe 现有重症 / Current Treatment 现有确诊 %'])
plt.savefig('CurrentCases.png')

#HB vs Rest
plt.figure(5)
hbNewConfirmed, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewConfirmed1_y']-dfChinaHB['NewWeakConfirmed16_y'], '--', linewidth=2, c='y')
restNewConfirmed, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewConfirmed1_x']-dfChinaHB['NewConfirmed1_y'], '-', linewidth=2, c='y')
hbNewSuspected, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSuspected5_y'], '--', linewidth=2, c='b')
restNewSuspected, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSuspected5_x']-dfChinaHBx['NewSuspected5_y'], '-', linewidth=2, c='b')
hbNewSevere, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSevere2_y'], '--', linewidth=2, c='r')
restNewSevere, = plt.plot(dfChinaHBx['Date'], dfChinaHBx['NewSevere2_x']-dfChinaHBx['NewSevere2_y'], '-', linewidth=2, c='r')
hbNewDischarged, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewDischarged4_y'], '--', linewidth=2, c='g')
restNewDischarged, = plt.plot(dfChinaHB['Date'], dfChinaHB['NewDischarged4_x']-dfChinaHB['NewDischarged4_y'], '-', linewidth=2, c='g')
plt.axis(("2/01", dfChina['Date'][nChina-1], -1000, 5000))
plt.xticks(dfChinaHB['Date'][::2], dfChinaHB['Date'][::2])
plt.xlabel('Date 日期')
plt.title('2019nCoV HuBei NewCases 湖北省新增')
plt.grid(True)
plt.legend([hbNewSuspected, restNewSuspected, hbNewConfirmed, restNewConfirmed, hbNewSevere, restNewSevere, hbNewDischarged, restNewDischarged], 
           [u'HuBei New Suspected 湖北省新增疑似', u'Rest New Suspected 其他各省新增疑似', u'HuBei New Confirmed 湖北省新增确诊', u'Rest New Confirmed 其他各省新增确诊', u'HuBei New Severe 湖北省新增重症', u'Rest New Severe 其他各省新增重症', u'HuBei New Discharged 湖北省新增治愈', u'Rest New Discharged 其他各省新增治愈'])
plt.savefig('HuBeiNewCases.png')

#Current HB vs Rest
plt.figure(6)
hbCurrentSuspected, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentSuspected11_y'], '--', linewidth=2, c='b')
restCurrentSuspected, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentSuspected11_x']-dfChinaHB0212['CurrentSuspected11_y'], '-', linewidth=2, c='b')
hbCurrentTreatment, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentTreatment15_y'], '--', linewidth=2, c='y')
restCurrentTreatment, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentTreatment15_x']-dfChinaHB0212['CurrentTreatment15_y'], '-', linewidth=2, c='y')
hbCurrentSevere, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentSevere7_y'], '--', linewidth=2, c='r')
restCurrentSevere, = plt.plot(dfChinaHB0212['Date'], dfChinaHB0212['CurrentSevere7_x']-dfChinaHB0212['CurrentSevere7_y'], '-', linewidth=2, c='r')
plt.axis(("2/12", dfChina['Date'][nChina-1], 0, 52000))
plt.xticks(dfChinaHB0212['Date'], dfChinaHB0212['Date'])
plt.xlabel('Date 日期')
plt.title('2019nCoV HuBei CurrentCases 湖北省现有')
plt.grid(True)
plt.legend([hbCurrentTreatment, restCurrentTreatment, hbCurrentSuspected, restCurrentSuspected, hbCurrentSevere, restCurrentSevere], 
           [u'HuBei Current Confirmed 湖北省现有确诊', u'Rest Current Confirmed 其他各省现有确诊', u'HuBei Current Suspected 湖北省现有疑似', u'Rest Current Suspected 其他各省现有疑似', u'HuBei Current Severe 湖北省现有重症', u'Rest Current Severe 其他各省现有重症'])
plt.savefig('HuBeiCurrentCases.png')

#plt.show()