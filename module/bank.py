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
        averageNumber = self.linkCSV[[' Gender', ' Credit_limit']].groupby(' Gender').agg(['mean', 'count'])
        averageRatio = self.linkCSV[[' Gender', ' Avg_utilities_ratio']].groupby(' Gender').agg(['mean', 'count'])
        return averageNumber, averageRatio

    def get_card_category(self):
        '''determining the type of cards according to the age of the client'''
        bank_cards = self.linkCSV.groupby(' Card_Category')
        self.maxAge = bank_cards[' Customer_age'].max()
        self.minAge = bank_cards[' Customer_age'].min()
        return self.maxAge, self.minAge, self.linkCSV.columns

    def __str__(self):
        return str(f'Code testing module:\n {self.get_test()} \
                   \n\nAverage number for a credit limit:\n {self.get_avg_limit()[0]} \
                   \n\nAvg utilities ratio:\n {self.get_avg_limit()[1]} \
                   \n\nMax Age:\n {self.get_card_category()[0]} \n\nMin Age:\n {self.get_card_category()[1]} \
                   \n\nAll columns:\n {self.get_card_category()[2]}')


if __name__ == '__main__':
    result = Bank()
    print(result)
