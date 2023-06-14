import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


class AnalisysML:

    def __init__(self):
        self.linkCSV = pd.read_csv('/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename_new.csv')
        # import pdb
        # pdb.set_trace()
        self.linkCSV[' Gender'] = self.linkCSV[' Gender'].map(self.get_gender)
        self.linkCSV[' Attrition_flag'] = self.linkCSV[' Attrition_flag'].map(self.get_customer)
        self.get_analisysML_preparations()
        self.get_data_set()
        self.get_save_pickle()

    def get_gender(self, x):
        '''conversion of data (gender) from a csv file into figures'''
        if x == 'male':
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
        lebel = LabelEncoder()
        lebel.fit(feat)
        # print(feat.name, lebel.classes_)
        return lebel.transform(feat)

    def get_analisysML_preparations(self):
        '''machine learning preparations'''
        self.y = self.linkCSV[' Card_category']
        self.X = self.linkCSV.copy()
        self.earnings = self.X[' Earnings'].value_counts()

        self.X[' Earnings'] = self.get_encoder(self.X[' Earnings'])
        self.X[' Education_level'] = self.get_encoder(self.X[' Education_level'])
        self.X[' Marital_status'] = self.get_encoder(self.X[' Marital_status'])

        # limit credit
        self.X = self.X.drop(['Customer_number', ' Card_category'], axis=1)

    def get_reduction(self):
        '''data dimension reduction'''
        self.pca = PCA(n_components=7)
        return self.pca.fit_transform(self.X), self.pca

    def get_data_set(self):
        '''building a test and training data set & ML'''
        Xtrain, Xtest, ytrain, ytest = train_test_split(self.get_reduction()[0], self.y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=300, n_jobs=-1)
        self.model.fit(Xtrain, ytrain)
        y_pred = self.model.predict(Xtest)
        self.random_model_accuracy_train = round(self.model.score(Xtrain, ytrain) * 100, 3)
        self.random_model_accuracy_tests = round(self.model.score(Xtest, ytest) * 100, 3)
        return self.random_model_accuracy_train, self.random_model_accuracy_tests, y_pred, self.model

    def get_save_pickle(self):
        pickle.dump(self.get_data_set()[3], open(
            '/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/BankCards.pickle', 'wb'))
        pickle.dump(self.get_reduction()[1], open(
            '/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv//BankCardsPCA.pickle', 'wb'))

    def __str__(self):
        # return f'{self.X.head(3)} {self.earnings} {self.X.describe()}'
        return f'Training data: {self.get_data_set()[0]} % \
                 \nTest data    : {self.get_data_set()[1]} %\n'


if __name__ == '__main__':
    ml = AnalisysML()
    print(ml)
