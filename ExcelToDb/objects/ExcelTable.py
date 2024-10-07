import pandas as pd
import numpy as np
import os
import openpyxl

from objects.Connection import Connection
from objects.DFReader import DFReader

from sql_requests import insert_update_sql_request, get_primary_key

from functions import get_db_credentials

class ExcelTable :

    def __init__(self, path_to_excel) :
        self.path = path_to_excel
        self.is_query_table = openpyxl.load_workbook(path_to_excel)
        self.name = os.path.splitext(os.path.basename(path_to_excel))[0]
        self.excel_df = DFReader(path_to_excel)
        self.excel_name = self.excel_df.get_file_name()
        

    def print_excel_table(self) :
        print(self.name)

    def get_path(self) :
        return self.path
    
    def get_is_query_table(self) :
        return self.is_query_table

    def get_name(self) :
        return self.name
    
    def get_excel_name(self) :
        return self.excel_name
    
    def get_excel_df(self) :
        return self.excel_df.get_df()
    
    def get_excel_columns(self) :
        return self.excel_df.get_columns()
    
    def get_database_table_mapping(self) :
        return self.excel_df.get_database_table_mapping()
    
    def excel_database_columns_mapper(self) :
        excel_columns = self.get_excel_columns()
        database_columns = ()
        path_to_columns_mapping_csv = r"ExcelToDb\ColumnsMapping\columns_mapping.csv"
        columns_mapping_df = DFReader(path_to_columns_mapping_csv).get_df()
        filtered_df = columns_mapping_df[columns_mapping_df["table"] == self.get_database_table_mapping()]
        excel_columns_mapping_df = filtered_df["excel_column"]
        database_columns_mapping_df = filtered_df["database_column"]
        for excel_column in excel_columns :
            if excel_column in excel_columns_mapping_df.to_list() :
                database_columns += (database_columns_mapping_df.loc[excel_columns_mapping_df == excel_column].iloc[0],)
            else :
                print("Excel column not found.")
        return database_columns

    def update_table_into_db(self) :
        excel_df = self.get_excel_df()
        tuple_df = [tuple(x) for x in excel_df.to_numpy()]
        table_name = self.get_database_table_mapping()
        database_columns = self.excel_database_columns_mapper()
        primary_key_sql_request = get_primary_key(table_name)
        
        db_credentials = get_db_credentials()
        if db_credentials is not None :
            connection = Connection(db_credentials)
            cursor = connection.get_cursor()
            cursor.execute(primary_key_sql_request)
            primary_key = tuple(column for sublist in cursor.fetchall() for column in sublist)
            upsert_sql_request = insert_update_sql_request(table_name, database_columns, primary_key)
            cursor.executemany(upsert_sql_request, tuple_df)
            connection.commit()
            connection.close()