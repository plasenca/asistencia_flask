import pandas as pd
import numpy as np

from pathlib import Path
from pandas import DataFrame
from pandas.errors import DtypeWarning

class DataManager:
    
    @staticmethod
    def reader_excel(data: Path) -> DataFrame:
        """Function to read a excel file
        
        Keyword arguments:
        data -- from class Path
        Return: Return a DataFrame
        """
        
        return pd.read_excel(data)
    
    @staticmethod
    def reader_csv(data: Path) -> DataFrame:
        """Function to read a .csv file
        
        Keyword arguments:
        data -- file path
        Return: Return a DataFrame
        """
        
        return pd.read_csv(data)
    
    @staticmethod
    def reader_data(data: Path) -> DataFrame:
        """
        Function to read data from .dat file.
        
        Keyword arguments:
        argument -- description
        Return: Return a dataframe.
        """ 
    
        return pd.read_csv(data, sep='\t', header=None)
    
    @staticmethod
    def to_format_time(data: Path, columns: list[str], format_time: str) -> None | DataFrame:
        """Function to format datetime to a specific format
        
        Keyword arguments:
        data    -- File path(.csv, .xlsx, .dat)
        columns -- Name columns with datetime object
        Return: Return None if it's not a accepted format. 
                Else, return a DataFrame
        """
        
        format_file = str(data).split(".")[-1]
        
        match format_file:
            case "csv":
                data = DataManager.reader_csv(data)
                
            case "xlsx":
                data = DataManager.reader_excel(data)
                
            case "dat":
                data = DataManager.reader_data(data)
                
            case _:
                raise DtypeWarning(f"It's not an accepted format.")

        i = 0
        while i < len(columns):
            data[columns[i]] = pd.to_datetime(data[columns[i]], format="%Y-%m-%d %H:%M:%S")
            i+=1

        return data

    def to_excel_file(data: DataFrame, filename="data"):
        """Function to convert a DataFrame to Excel file
        
        Keyword arguments:
        data -- File Path
        Return: A Excel File
        """
        
        if isinstance(data, DataFrame):
            data.to_excel(f"{filename}.xlsx")
        else:
            raise DtypeWarning("It's not a DataFrame")
        
if __name__ == "__main__":
    DataManager.to_excel_file(data="asd",filename="Hola")