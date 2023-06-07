import os, glob


def get_clear_dir():
    '''Function clining of csv dir'''

    dir_csv = '/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv'

    filelistMain = glob.glob(os.path.join(dir_csv, "*"))

    for files in filelistMain:
        os.remove(files)

get_clear_dir()
