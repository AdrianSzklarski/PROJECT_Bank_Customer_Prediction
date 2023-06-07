import numpy as np
import pandas as pd

from module.clearDir import get_clear_dir

'''Class that creates a csv file with data of bank customers'''


class DataCSV:
    def __init__(self):
        get_clear_dir()
        self.get_client()
        self.get_clear_csv()

    def get_client(self):
        ''' Function to build random data for analysis in *.*csv file
        :param scope of random choice
        :rtype int, str
        :return *.*csv file of Data Frame
        '''

        row_of_title = [
            'Customer number',
            'Customer age',
            'Gender',
            'Number of counts',
            'Education level',
            'Marital status',
            'Earnings',
            'Card Category',
            'Credit limit'
        ]

        for i in range(1, 101):
            '''Create data to csv file'''
            customer_number = np.random.randint(100000000, 999999999, 1)
            customer_age = np.random.randint(18, 64)
            number_of_counts = np.random.randint(1, 6, 1)
            earnings = np.random.randint(2500, 32000)

            WORDS = ('male', 'female')
            gender = np.random.choice(WORDS)

            EDU = ('high school', 'Collage', 'Graduate', 'Doctorate', 'Professor', 'Unknown', 'Post-Graduate',
                   'Uneducated', 'Student')
            education_level = np.random.choice(EDU)

            STATUS = ('Single', 'Married', 'Unknown')
            marital_status = np.random.choice(STATUS)

            if 2500 <= earnings < 5000:
                card_category = 'White'
                credit_limit = 2500 * 1.5
            elif 5000 <= earnings < 7500:
                card_category = 'Black'
                credit_limit = 5000 * 1.58
            elif 7500 <= earnings < 12000:
                card_category = 'Silver'
                credit_limit = 7500 * 1.82
            elif 12000 <= earnings <= 18000:
                card_category = 'Gold'
                credit_limit = 12000 * 2.05
            else:
                card_category = 'Platinum'
                credit_limit = 18000 * 2.47

            self.df = pd.DataFrame(data=[[customer_number, customer_age, gender, number_of_counts,
                                          education_level, marital_status, f'{earnings} zł brutto',
                                          card_category, credit_limit]], index=[f'{i}'], columns=row_of_title)

            with open('../csv/filename.csv', 'a', newline="", encoding='UTF-8') as csv_file:
                self.df.to_csv(path_or_buf=csv_file)

    def get_clear_csv(self):
        ''' Compilation of *.*csv file based on source data
        :param input file
        :return new *.*csv file
        '''

        link_csv = '/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename.csv'
        link_csv_new = '/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/filename_new.csv'
        with open(link_csv, 'r') as f:
            line_count = 0
            for i in f:
                if line_count == 0:
                    head = f'{"".join(i)}'
                    with open(link_csv_new, 'a', newline="", encoding='UTF-8') as csv_file_new:
                        csv_file_new.write(head)
                    line_count += 1
                elif line_count % 2 == 0:
                    with open(link_csv_new, 'a', newline="", encoding='UTF-8') as csv_file_new:
                        csv_file_new.write(i)
                line_count += 1


if __name__ == '__main__':
    DataCSV()
