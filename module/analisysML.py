import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA


class AnalisysML:

    def __init__(self):
        self.linkCSV = pd.read_csv('/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename_new.csv')
        # import pdb
        # pdb.set_trace()
        self.linkCSV[' Gender'] = self.linkCSV[' Gender'].map(self.get_gender)
        self.linkCSV[' Attrition_flag'] = self.linkCSV[' Attrition_flag'].map(self.get_customer)
        self.get_analisysML_preparations()

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

    def get_analisysML_preparations(self):
        '''machine learning preparations'''
        self.y = self.linkCSV[' Card_category']
        self.X = self.linkCSV.copy()
        self.earnings = self.X[' Earnings'].value_counts()

        self.X[' Earnings'] = self.get_encoder(self.X[' Earnings'])
        self.X[' Education_level'] = self.get_encoder(self.X[' Education_level'])
        self.X[' Marital_status'] = self.get_encoder(self.X[' Marital_status'])

        # limit credit
        # information in my notebook
        self.X = self.X.drop([' Customer_number', ' Card_category'], axis=1)

    def get_reduction(self):
        '''data dimension reduction'''
        pca = PCA(n_components=7)
        pca2 = PCA(n_components=10)
        return pca.fit_transform(self.X), pca2.fit_transform(self.X)

    def __str__(self):
        return f'{self.X.head(3)} {self.earnings} {self.X.describe()}'


if __name__ == '__main__':
    ml = AnalisysML()
    print(ml)
