from module.bank import Bank
from module.preparationCSV import DataCSV
from module.clearDir import get_clear_dir
import os

if __name__ == '__main__':
    dir = os.listdir('/home/adrian/Pulpit/GitHub_Public/Bank_Customers_Prediction/csv')
    if len(dir) == 0:
        try:
            DataCSV()
            result = Bank()
            print(result)
            print('The program to create *.*csv is started, empty directory "csv"')
        except FileNotFoundError as e:
            print(e)
    else:
        get_clear_dir()
        DataCSV()
        result = Bank()
        print(result)
        print('The *.*csv creation program was started, the "csv" directory was cleared')


