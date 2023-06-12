import pandas as pd
from sklearn.preprocessing import LabelEncoder


class AnalisysML:

    def __init__(self):
        self.linkCSV = pd.read_csv('/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename_new.csv')
        # import pdb
        # pdb.set_trace()
        self.linkCSV[' Gender'] = self.linkCSV[' Gender'].map(self.get_gender)
        self.linkCSV[' Attrition_flag'] = self.linkCSV[' Attrition_flag'].map(self.get_customer)
        self.y = self.linkCSV[' Card_Category']
        self.X = self.linkCSV.copy()
        self.earnings = self.X[' Earnings'].value_counts()

        self.X[' Earnings'] = self.get_encoder(self.X[' Earnings'])
        self.X[' Education_level'] = self.get_encoder(self.X[' Education_level'])
        self.X[' Marital_status'] = self.get_encoder(self.X[' Marital_status'])

    def get_gender(self, x):
        '''conversion of data (gender) from a csv file into figures'''
        if x == 'male ':
            return 1
        else:
            return 0

    def get_customer(self, x):
        '''conversion of data (customer) from a csv file into figures'''
        if x == 'Existing Customer':
            return 1
        else:
            return 0

    def get_encoder(self, feat):
        '''conversion of categorical data into numerical data'''
        le = LabelEncoder()
        le.fit(feat)
        print(feat.name, le.classes_)
        return le.transform(feat)


    def __str__(self):
        return f'{self.X.head(3)} {self.earnings} {self.X.describe()}'


if __name__ == '__main__':
    ml = AnalisysML()
    print(ml)
