import subprocess, sys, os

from datetime import datetime

from functions import navigate_through_folders, get_all_excel_files, get_db_credentials
from objects.ExcelTable import ExcelTable
from objects.Connection import Connection

def exit() :
    return

def update_database() :
    accepted_file_extension = ".xlsx"
    default_path = r"C:\Users\tompi\Desktop\Tom\Auto Entreprise\EXCEL"
    path_to_excel_table = navigate_through_folders(default_path, accepted_file_extension)
    excel_table = ExcelTable(path_to_excel_table)
    excel_table.update_table_into_db()

def update_all_tables() :
    excel_files_list = get_all_excel_files("EXCEL")
    for excel_file in excel_files_list :
        excel_table = ExcelTable(excel_file)
        print(excel_table.get_name(), excel_table.get_excel_name(), excel_table.get_path(), excel_table.get_is_query_table().sheetnames[0].lower())

def dump_database() :
    try:
        db_credentials = get_db_credentials()
        if db_credentials is not None :
            connection = Connection(db_credentials)
            path_to_output_file = r"C:\Users\tompi\Desktop\Tom\Auto Entreprise\SQL\Dump"
            file_name = "dump_" + datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".backup"
            command = [
                r"C:\Program Files\PostgreSQL\16\bin\pg_dump",
                '-h', connection.get_host(),
                '-p', connection.get_port(),
                '-U', connection.get_user(),
                '-d', connection.get_database(),
                '-Fc',
                '-f', os.path.join(path_to_output_file, file_name)
            ]

        subprocess.run(command, check = True)
        print(f"Dump file has been successfully created : {path_to_output_file}")
        connection.close()

    except subprocess.CalledProcessError as e:
        print(f"Error while creating dump file : {e}")
        connection.close()
        sys.exit(1)

def restore_database() :
    try:
        db_credentials = get_db_credentials()
        if db_credentials is not None :
            connection = Connection(db_credentials)
            accepted_file_extension = ".backup"
            path_to_dump_folder = r"C:\Users\tompi\Desktop\Tom\Auto Entreprise\SQL\Dump"
            path_to_restoration_file = navigate_through_folders(path_to_dump_folder, accepted_file_extension)
            command = [
                r"C:\Program Files\PostgreSQL\16\bin\pg_restore",
                '-h', connection.get_host(),
                '-p', connection.get_port(),
                '-U', connection.get_user(),
                '-d', connection.get_database(),
                '-Fc',
                '-v', path_to_restoration_file
            ]

        subprocess.run(command, check = True)
        print(f"The database has been successfully restored with : {path_to_restoration_file}")
        connection.close()

    except subprocess.CalledProcessError as e:
        print(f"Error while trying to restore the database : {e}")
        connection.close()
        sys.exit(1)

def test() :
    activity_report = r"EXCEL\CRA\2023.xlsx"
    mission = r"EXCEL\TJM\Mission.xlsx"
    excel_table = ExcelTable(activity_report).get_excel_df()
    linux_command_dump = r'pg_dump -h localhost -p 5432 -U postgres -d postgres -F c -f "C:\Users\tompi\Desktop\Tom\Auto Entreprise\SQL\Dump\dump.backup"'
    linux_command_restore = r'pg_restore -h localhost -U postgres -d postgres -F c -v "C:\Users\tompi\Desktop\Tom\Auto Entreprise\SQL\Dump\dump.backup"'
