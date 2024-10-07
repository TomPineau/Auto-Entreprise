import os
import numpy as np

from objects.DFReader import DFReader
    
def get_menu_information() :
    menu_message = "Select an option :\n"
    csv = DFReader("ExcelToDb\menu.csv").get_df()
    n, p = np.shape(csv)
    id_column = csv["id"].to_list()
    detail_column = csv["detail"].to_list()
    function_column = csv["function"].to_list()
    for i in range(n) :
        menu_message += id_column[i] + " - " + detail_column[i] + "\n"
    return csv, id_column, detail_column, function_column, menu_message

def get_db_credentials() :
    path_to_db_credentials_csv = "ExcelToDb\db_credentials.csv"
    df = DFReader(path_to_db_credentials_csv).get_df()
    id_environment_list = df["id"].tolist()
    db_credentials_message = "To which environment do you want to connect ? Press -1 if you want to exit.\n"
    for id in df["id"] :
        db_credentials_message += "\t" + id + " - " + df["environment"][df["id"] == id].values[0] + "\n"
    print(db_credentials_message)
    option = input()
    while option not in id_environment_list and option not in ["-1"]:
        print("This option is not correct, please try again.")
        print(db_credentials_message)
        option = input()
    if option == "-1" :
        return
    elif option in id_environment_list :
        return df[df["id"] == option]
    
def navigate_through_folders(path, accepted_file_extension) :
    min_path = r"C:\Users\tompi\Desktop\Tom\Auto Entreprise"
    if min_path not in path :
        path = min_path
    elements_list_in_current_folder = os.listdir(path)
    accepted_elements_list = []
    for element in elements_list_in_current_folder :
        path_to_file = os.path.join(path, element)
        if os.path.isdir(path_to_file) :
            accepted_elements_list.append(element)
        else :
            if not element.startswith("~$") and element.endswith(accepted_file_extension) :
                accepted_elements_list.append(element)
    n = len(accepted_elements_list)
    if n <= 0 :
        print("No file or folder found, please try again.")
        previous_path = os.path.dirname(path)
        return navigate_through_folders(previous_path, accepted_file_extension)
    else :
        option_message = "Select a file or a folder :\n"
        for i in range(n) :

            element = accepted_elements_list[i]
            option_message += "\t" + str(i + 1) + " - " + element + "\n"
        print(option_message)
        option = input()
        option_index_list = [str(i) for i in range(-1, n + 1)]
        while option not in option_index_list :
            print("This option is not correct, please try again.")
            print(option_message)
            option = input()
        if option == "-1" :
            return
        elif option == "0" :
            previous_path = os.path.dirname(path)
            return navigate_through_folders(previous_path, accepted_file_extension)
        else :
            next_element = accepted_elements_list[int(option) - 1]
            next_path = os.path.join(path, next_element)
            if os.path.isdir(next_path) :
                return navigate_through_folders(next_path, accepted_file_extension)
            elif os.path.isfile(next_path) :
                option_message = "Do you want to select this file : " + next_path + " (y/n) ?"
                print(option_message)
                option = input()
                while option not in ["y", "n"]:
                    print("This option is not correct, please try again.")
                    print(option_message)
                    option = input()
                if option == "y" :
                    print(next_path)
                    return next_path
                elif option == "n" :
                    return navigate_through_folders(path, accepted_file_extension)
            else :
                print("wtf")

def get_all_excel_files(start_path):
    excel_files_list = []
    for root_folder, _, files in os.walk(start_path):
        for file in files:
            if file.endswith('.xlsx') and not file.startswith("~$") :
                chemin_complet = os.path.join(root_folder, file)
                excel_files_list.append(chemin_complet)
    return excel_files_list