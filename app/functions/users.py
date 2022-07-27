import pandas as pd

class UsersDataFrame():
    
    @classmethod
    def dictionary_user(id_employee, name_employee) -> dict:
        return {'id_employee': id_employee, 'name_employee': name_employee}
    
    @classmethod
    def dataframe_initial(self, user_dict) -> pd.DataFrame:
        return pd.DataFrame(user_dict, columns=['employee_id', 'employee_name'])

    def __call__(self, *args, **kwargs):
        data_frame = self.dictionary_user(*args, **kwargs)
        return self.dataframe_initial(data_frame)

class EmployeeMainOffice(UsersDataFrame):
    
    def __init__(self) -> None:
        self.id_employee: list   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.name_employee: list = ["Jacinto", "Yefran", "Cindy", "Alexis", 
                        "Juan Carlos Plasencia", "Miguel Curo", "Giuliana",
                        "Danna", "Felix Silva", "Franklin Velasquez", "Magda Paniura",
                        "Uriel Chipana", "Franzua Plasencia", "Santiago", "Wildor Paniura",
                        "Enaida", "Ronald", "Anthony V"]

    def __str__(self):
        print(UsersDataFrame.__call__(self.id_employee, self.name_employee))

class EmployeeNicolinni(UsersDataFrame):
    
    def __init__(self) -> None:
        self.id_employee: list   = [1, 2, 3]
        self.name_employee: list = ["Claudia Santilla", "Luis Perez", "Rolando"]
        
        self.dictionary_users = {'employee_id': self.id_employee,
                                'employee_name': self.name_employee}

    def dataframe_initial(self) -> pd.DataFrame:
        return pd.DataFrame(self.dictionary_users, columns=['employee_id', 'employee_name'])


if __name__ == '__main__':
    users = EmployeeMainOffice()
    print(users)

