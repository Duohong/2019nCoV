from datetime import datetime, timedelta
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

def main():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    dfData = pd.read_csv('data.csv')
    dfChina = dfData[dfData['Region']=='China']
    nChina = len(dfChina)

    dfCountries = pd.read_csv('countries.csv')
    nCountries = len(dfCountries)
    dfSK = dfCountries[dfCountries['Date']<='4/24']

    dfNY = pd.read_csv('newYork.csv')
    dfNYR = dfNY[dfNY['Date']>='3/11']
    startNYR = len(dfNY)-len(dfNYR)
    endNYR = len(dfNY) - 1

    xTicks = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
    xLabels = ["10", "30", "100", "300", "1k", "3k", "10k", "30k", "100k", "300k", "1m"]
    yTicks = [0, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]
    yLabels = ["0", "1", "3", "10", "30", "100", "300", "1k", "3k", "10k", "30k", "100k"]

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
    plt.yscale('symlog')
    plt.axis((dfCountries['Date'][0], dfCountries['Date'][nCountries-1], 0, 100000))
    plt.xticks(dfCountries['Date'][::3], dfCountries['Date'][::3], rotation='vertical')
    plt.xlabel('Date 日期')
    plt.yticks(yTicks, yLabels)
    plt.title('COVID-19 Daily New Cases 每日新增确诊')
    plt.grid(True)
    plt.subplots_adjust(left=0.08, bottom=0.16, right=0.95)
    plt.gca().yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
    plt.gca().yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.legend([china, sk, iran, italy, spain, us], [u'China 中国', u'South Korea 韩国', u'Iran 伊朗', u'Italy 意大利', u'Spain 西班牙', u'US 美国'])
    plt.savefig('Countries.png')

    #CountryMillion
    plt.figure(12)
    china, = plt.plot(dfChina['Date'], dfChina['NewConfirmed1']*1000//1393, '-', linewidth=2, c='r')
    sk, = plt.plot(dfSK['Date'], dfSK['South Korea']*1000//52, '-', linewidth=2, c='black')
    iran, = plt.plot(dfCountries['Date'], dfCountries['Iran']*1000//82, '-', linewidth=2, c='y')
    italy, = plt.plot(dfCountries['Date'], dfCountries['Italy']*1000//60, '-', linewidth=2, c='g')
    spain, = plt.plot(dfCountries['Date'], dfCountries['Spain']*1000//47, '-', linewidth=2, c='orange')
    us, = plt.plot(dfCountries['Date'], dfCountries['US']*1000//328, '-', linewidth=2, c='b')
    plt.yscale('symlog')
    plt.axis((dfCountries['Date'][0], dfCountries['Date'][nCountries-1], 0, 100000))
    plt.xticks(dfCountries['Date'][::3], dfCountries['Date'][::3], rotation='vertical')
    plt.xlabel('Date 日期')
    plt.yticks([0, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000], \
               ["0", "0.001", "0.003", "0.01", "0.03", "0.1", "0.3", "1", "3", "10", "30", "100", "300"])
    plt.title('COVID-19 Daily New Cases Per Million People 每日新增确诊每百万人口')
    plt.grid(True)
    plt.subplots_adjust(left=0.08, bottom=0.16, right=0.95)
    plt.gca().yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
    plt.gca().yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.legend([china, sk, iran, italy, spain, us], [u'China 中国', u'South Korea 韩国', u'Iran 伊朗', u'Italy 意大利', u'Spain 西班牙', u'US 美国'])
    plt.savefig('CountryMillion.png')

    #Log Countries
    plt.figure(20)
    china = plotCountry(dfChina['NewConfirmed1'], 1287-444, 'r')
    sk = plotCountry(dfCountries['South Korea'], 0, 'black')
    iran = plotCountry(dfCountries['Iran'], 0, 'y')
    italy = plotCountry(dfCountries['Italy'], 0, 'g')
    spain = plotCountry(dfCountries['Spain'], 0, 'orange')
    us = plotCountry(dfCountries['US'], 0, 'b')
    plt.xscale('symlog')
    plt.yscale('symlog')
    plt.axis((10, 300000, 3, 30000))
    plt.xlabel('Daily Cumulative Sum 每日累计确诊')
    plt.xticks(xTicks, xLabels)
    plt.ylabel('Daily New Cases 每日新增确诊')
    plt.yticks(yTicks[2:], yLabels[2:])
    plt.title('COVID-19 Daily Countries 每日各国')
    plt.grid(True)
    plt.subplots_adjust(left=0.12, right=0.95, bottom=0.1)
    xaxis, yaxis = plt.gca().xaxis, plt.gca().yaxis
    xaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
    xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(1,2,3,4,5,6,7,8,9,10) ) )
    yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.legend([china, sk, iran, italy, spain, us], [u'China 中国', u'South Korea 韩国', u'Iran 伊朗', u'Italy 意大利', u'Spain 西班牙', u'US 美国'])
    plt.savefig('DailyCountries.png')

    #plt.show()
    return 

if __name__ == '__main__':
    main()
