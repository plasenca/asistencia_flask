import pandas as pd


class EmployeeCoinp(object):
    
    def __init__(self) -> pd.DataFrame:
        self.id_employee: list   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.name_employee: list = ["Jacinto", "Yefran", "Cindy", "Alexis", 
                        "Juan Carlos Plasencia", "Miguel Curo", "Giuliana",
                        "Danna", "Felix Silva", "Franklin Velasquez", "Magda Paniura",
                        "Uriel Chipana", "Franzua Plasencia", "Santiago", "Wildor Paniura",
                        "Enaida", "Ronald", "Anthony V"]
        
        self.dictionary_users = {'employee_id': self.id_employee,
                                'employee_name': self.name_employee}

    def dataframe_initial(self) -> pd.DataFrame:
        return pd.DataFrame(self.dictionary_users, columns=['employee_id', 'employee_name'])




if __name__ == '__main__':
    users = EmployeeCoinp().dataframe_initial()
    print(users.employee_id)


