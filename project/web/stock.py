import os
import pandas as pd
import time
import datetime
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=NjEc7PB0TxQ https://youtu.be/fw4gK-leExw
class Stock():
    def create_stock(str):
        ticker = '' +str
        period1 = int(time.mktime(datetime.datetime(2022, 9, 1, 23, 59).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2022, 9, 30, 23, 59).timetuple()))

        interval = '1d'  # 1wk, 1d, 1m
        my_path = os.path.abspath(__file__)


        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true '

        open = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(1,))},
                            index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))
        high = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(2,))},
                            index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))
        low = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(3,))},
                           index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))
        close = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(4,))},
                             index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))
        adj_Close = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(5,))},
                                 index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))
        volume = pd.DataFrame({'values': np.genfromtxt(query_string, delimiter=',', names=True, usecols=(6,))},
                              index=pd.date_range(start='2022-09-01', end='2022-09-30', freq='B'))

        plt.rcParams["figure.figsize"] = (8, 5)
        fig, ax = plt.subplots()
        fig.subplots_adjust
        # fig.tight_layout()

        # fig.suptitle('Dynagas LNG Partners LP [DLNG] Stock Prices for September 2022 ')
        # fig.tight_layout(pad=7.0)

        monthyearFmt = mdates.DateFormatter('%Y %B')

        ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        ax.plot(open.index, open.values, color='r', label='Open')
        ax.plot(high.index, high.values, color='g', label='High')
        ax.plot(low.index, low.values, color='b', label='Low')
        ax.plot(close.index, close.values, color='y', label='Close')
        ax.plot(adj_Close.index, adj_Close.values, color='k', label='Adj Close')
        # ax.set_title('Open, High, Low, Close, Adj Close')
        ax.set_xlabel('Days')
        ax.set_ylabel('Currency in USD')
        # plt.subplots_adjust(top=0.9, wspace=0.1)
        # plt.text(x=0.5, y=0.94, s="Dynagas LNG Partners LP [DLNG] Stock Prices for September 2022", fontsize=35,
        # ha="center",    transform=fig.transFigure)

        plt.savefig(my_path + '/static/stock/{ticker}.png')  # beta
        plt.legend()
        # plt.show()
