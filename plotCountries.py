from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

#mpl.rcParams['font.family']="SimHei"
#mpl.rcParams['axes.unicode_minus']=False # in case minus sign is shown as box

mpl.rcParams.update(
    {
        'text.usetex': False,
        #'font.family': 'stixgeneral',
        'font.family': 'SimHei',
        'axes.unicode_minus': False,
        'mathtext.fontset': 'stix',
    }
)

dfData = pd.read_csv('data.csv')
dfChina = dfData[dfData['Region']=='China']
nChina = len(dfChina)

dfCountries = pd.read_csv('countries.csv')
nCountries = len(dfCountries)
dfSK = dfCountries[dfCountries['Date']<='4/08']

xTicks = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
yTicks = [0, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]

def plotCountry(dfCol, startTotal, color):
    startTotal
    totalList = []
    for v in dfCol:
        startTotal += v
        totalList.append(startTotal)
    ans, = plt.plot(totalList, dfCol, '-', linewidth=1, c=color)
    return ans

#Countries
plt.figure(1)
china, = plt.plot(dfChina['Date'], dfChina['NewConfirmed1'], '-', linewidth=2, c='r')
sk, = plt.plot(dfSK['Date'], dfSK['South Korea'], '-', linewidth=2, c='black')
iran, = plt.plot(dfCountries['Date'], dfCountries['Iran'], '-', linewidth=2, c='y')
italy, = plt.plot(dfCountries['Date'], dfCountries['Italy'], '-', linewidth=2, c='g')
spain, = plt.plot(dfCountries['Date'], dfCountries['Spain'], '-', linewidth=2, c='orange')
us, = plt.plot(dfCountries['Date'], dfCountries['US'], '-', linewidth=2, c='b')
#germany, = plt.plot(dfCountries['Date'], dfCountries['Germany'], '-', linewidth=2, c='m')
plt.yscale('symlog')
plt.axis((dfCountries['Date'][0], dfCountries['Date'][nCountries-1], 0, 100000))
plt.xticks(dfCountries['Date'][::3], dfCountries['Date'][::3], rotation='vertical')
plt.xlabel('Date 日期')
plt.yticks(yTicks, yTicks)
plt.title('COVID-19 Daily New Cases 每日新增确诊')
plt.grid(True)
plt.subplots_adjust(bottom=0.16)
plt.gca().yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
plt.gca().yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
plt.gca().yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
plt.legend([china, sk, iran, italy, spain, us], [u'China 中国', u'South Korea 韩国', u'Iran 伊朗', u'Italy 意大利', u'Spain 西班牙', u'US 美国'])
plt.savefig('Countries.png')

#Log Countries
plt.figure(2)
china = plotCountry(dfChina['NewConfirmed1'], 1287-444, 'r')
sk = plotCountry(dfCountries['South Korea'], 0, 'black')
iran = plotCountry(dfCountries['Iran'], 0, 'y')
italy = plotCountry(dfCountries['Italy'], 0, 'g')
spain = plotCountry(dfCountries['Spain'], 0, 'orange')
us = plotCountry(dfCountries['US'], 0, 'b')
#germany = plotCountry(dfCountries['Germany'], 0, 'm')
plt.xscale('symlog')
plt.yscale('symlog')
plt.axis((10, 300000, 3, 30000))
plt.xlabel('Daily Cumulative Sum 每日累计确诊')
plt.xticks(xTicks, xTicks)
plt.ylabel('Daily New Cases 每日新增确诊')
plt.yticks(yTicks[2:], yTicks[2:])
plt.title('COVID-19 Daily Countries 每日各国')
plt.grid(True)
plt.subplots_adjust(bottom=0.1)
xaxis, yaxis = plt.gca().xaxis, plt.gca().yaxis
xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
xaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
plt.legend([china, sk, iran, italy, spain, us], [u'China 中国', u'South Korea 韩国', u'Iran 伊朗', u'Italy 意大利', u'Spain 西班牙', u'US 美国'])
plt.savefig('DailyCountries.png')

#plt.show()
