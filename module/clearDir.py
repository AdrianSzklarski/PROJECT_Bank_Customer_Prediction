import os, glob


def get_clear_dir():
    '''Function clining of csv dir'''

    filelistMain = glob.glob(r'/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv/*.csv')

    for files in filelistMain:
        os.remove(files)

get_clear_dir()
