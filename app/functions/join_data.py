from users import EmployeeNicolinni
from reader_data import read_dat
import pandas as pd
from constants import BASE_PATH

def join_data(UserClass_=None, _path=None, data_path=None, **kwargs):
    """
    Join data from dataframes and export the joined file to .xlsx file.
    
    Keyword arguments:
    @param UserClass_: Class of the users dataframe.
    @param _path: Path of the file to be exported.
    @param data_path: Path of the data to be joined.
    @param kwargs: Keyword arguments to be passed to join the dataframe.
    Return: Dataframe with joined data.
    """
    
    users = UserClass_().dataframe_initial()
    data = read_dat(data_path)
    data.columns = ['employee_id', 'arrive_time', 
                        'rubbish_1', 'rubbish_2', 
                        'rubbish_3', 'rubbish_4']
    
    data_joined = pd.merge(users, data, how = kwargs["how"] ,
                            left_on = kwargs["left_on"] , right_on = kwargs["right_on"])
    data_joined.to_excel(_path, index=False)
    
if __name__ == '__main__':
    # _path = BASE_PATH / 'data' / 'data_joined.xlsx'
    # data_path = BASE_PATH / 'data' / 'data.dat'
    
    # join_data(_path, data_path, how="outer", left_on = 'employee_id', right_on = 'employee_id')
    
    _path = BASE_PATH / 'data' / 'data_joined_nicolini.xlsx'
    data_path_nicolini = BASE_PATH / 'data' / 'data_nicolini.dat'
    
    join_data(EmployeeNicolinni ,_path, data_path_nicolini, how="outer", left_on = 'employee_id', right_on = 'employee_id')
