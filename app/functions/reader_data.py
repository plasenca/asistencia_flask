import pandas as pd
from constants import BASE_PATH

def read_dat(file_name):
    """
    Function to read data from .dat file.
    
    Keyword arguments:
    argument -- description
    Return: Return a dataframe.
    """
    
    data = pd.read_csv(file_name, sep='\t', header=None)
    
    return data
#TODO: Crear un string con respecto a la dirección del USB.


if __name__ == '__main__':
    data_raw:pd.DataFrame = read_dat(BASE_PATH / 'data' / 'data.dat')
    data_raw.columns = ['employee_id', 'arrive_time', 
                        'rubbish_1', 'rubbish_2', 
                        'rubbish_3', 'rubbish_4']
    print(data_raw.employee_id)
    print("Success")
    