import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Bank:
    def __init__(self):
        self.linkCSV = pd.read_csv('/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename_new.csv')
        self.get_chart()

    def get_test(self):
        '''Code testing module'''

        dataReview = self.linkCSV.head(50), \
                     self.linkCSV.shape, \
                     self.linkCSV.isnull().sum()
        return dataReview

    def get_chart(self):
        '''Understanding about some columns first'''
        sns.set_theme(style="whitegrid")
        sns.boxplot(self.linkCSV[[' Customer_age']])
        plt.show()

    def get_avg_limit(self):
        '''average number for a credit limit'''
        return self.linkCSV[[' Gender', ' Credit_limit']].groupby(' Gender').agg(['mean', 'count'])

    def __str__(self):
        return str(f'Code testing module:\n {self.get_test()} \
                   \n\nAverage number for a credit limit:\n {self.get_avg_limit()}')


if __name__ == '__main__':
    result = Bank()
    print(result)
