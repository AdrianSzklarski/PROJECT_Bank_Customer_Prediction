import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

''' The class prepares data for Machine Learning analysis based on data obtained from *.*csv file'''


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

    def get_analisys_card(self):
        '''determining the type of cards according to the age of the client'''
        bank_cards = self.linkCSV.groupby(' Card_Category')
        bank_marital = self.linkCSV.groupby(' Marital_status')

        # analysis for different age groups
        self.maxAge = bank_cards[' Customer_age'].max()
        self.minAge = bank_cards[' Customer_age'].min()

        # average for all card ratios
        self.ave = bank_cards[' Avg_utilities_ratio'].mean()

        # analysis for different civil statuses
        self.marital = bank_marital[' Card_Category'].value_counts()

        return self.maxAge, self.minAge, self.linkCSV.columns, self.ave, self.marital

    def get_bank_customers(self):
        '''analysis of active and inactive bank customers
        Attrited Customer: the customer closed his account
        Existing Customer: customer who has an activated account

        The following can be used to build the model:
        1. remove inactive customers;
        2. leave active and inactive customers;
        Solution 2 has been used in the model.
        '''
        self.customers = self.linkCSV[' Attrition_flag'].value_counts()
        self.gender = self.linkCSV[' Gender'].value_counts()
        self.education = self.linkCSV[' Education_level'].value_counts()
        self.marital = self.linkCSV[' Marital_status'].value_counts()
        return self.customers, self.gender, self.education, self.marital

    def __str__(self):
        return str(f'Code testing module:\n {self.get_test()} \
                   \n\nAverage number for a credit limit:\n {self.get_avg_limit()[0]} \
                   \n\nAvg utilities ratio:\n {self.get_avg_limit()[1]} \
                   \n\nMax Age:\n {self.get_analisys_card()[0]} \n\nMin Age:\n {self.get_analisys_card()[1]} \
                   \n\nAll columns:\n {self.get_analisys_card()[2]} \
                   \n\nAverage for all card ratios:\n {self.get_analisys_card()[3]} \
                   \n\nAnalysis for different civil statuses:\n {self.get_analisys_card()[4]} \
                   \n\nActive and inactive bank customers:\n {self.get_bank_customers()[0]} \
                   \nand their gender{self.get_bank_customers()[1]} \
                   \nand their education{self.get_bank_customers()[2]} \
                   \nand their marital{self.get_bank_customers()[1]}')


if __name__ == '__main__':
    result = Bank()
    print(result)
