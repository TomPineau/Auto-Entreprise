import os
import pandas as pd
import numpy as np

class DFReader :

    def __init__(self, path_to_df) :
        self.df = None
        self.sheetnames = None
        self.database_table_mapping = None
        self.folder_name = os.path.basename(os.path.dirname(path_to_df))
        self.file_name, self.extension = os.path.splitext(os.path.basename(path_to_df))
        if self.extension == ".xlsx" :
            excel_file = pd.ExcelFile(path_to_df)
            self.sheetnames = excel_file.sheet_names
            excels_mapping_csv = DFReader(r"ExcelToDb\ExcelsMapping\excels_mapping.csv").get_df()
            folder_filter = excels_mapping_csv["folder"] == self.folder_name
            file_filter = excels_mapping_csv["excel_name"] == self.file_name
            filtered_df = excels_mapping_csv[folder_filter & file_filter]
            allowed_sheets = filtered_df["excel_sheet"]
            if len(allowed_sheets) > 1 :
                sheet_df_list = []
                for sheetname in allowed_sheets.to_list() :
                    if sheetname in self.sheetnames :
                        sheet_df_list.append(excel_file.parse(sheetname))
                self.df = pd.concat(sheet_df_list, ignore_index = True)#.astype('str')
            else :
                self.df = pd.read_excel(path_to_df, header = 0, dtype = str)
            self.df = self.df.replace({np.nan: None})
            self.database_table_mapping = filtered_df["database_table"].iloc[0]
            excel_file.close()
        elif self.extension == ".csv" :
            self.df = pd.read_csv(path_to_df, sep = "|", header = 0, dtype = str, encoding = "utf-8")
        else :
            print("Unrecognized file extension.")
            return
        self.columns = tuple(self.df.columns.to_list())

    def get_folder_name(self) :
        return self.folder_name
    
    def get_database_table_mapping(self) :
        return self.database_table_mapping
    
    def get_file_name(self) :
        return self.file_name
    
    def get_extension(self) :
        return self.extension

    def get_df(self) :
        return self.df
    
    def get_sheetnames(self) :
        return self.sheetnames
    
    def get_columns(self) :
        return self.columns