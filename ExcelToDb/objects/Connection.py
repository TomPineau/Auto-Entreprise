import psycopg2

class Connection :

    def __init__(self, db_credentials) :
        self.database = db_credentials["database"].values[0]
        self.schema = db_credentials["schema"].values[0]
        self.host = db_credentials["host"].values[0]
        self.port = db_credentials["port"].values[0]
        self.user = db_credentials["user"].values[0]
        self.password = db_credentials["password"].values[0]
        self.connection = None
        self.cursor = None
        try :
            self.connection = psycopg2.connect(
                database = self.database,
                options = f'-c search_path={self.schema}',
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password
            )
            self.cursor = self.connection.cursor()
            print("Connection successful !")

        except psycopg2.Error as e:
            print("Error while trying to connect :", e)

    def get_database(self) :
        return self.database
    
    def get_schema(self) :
        return self.schema
    
    def get_host(self) :
        return self.host
    
    def get_port(self) :
        return self.port
    
    def get_user(self) :
        return self.user
    
    def get_password(self) :
        return self.password
    
    def get_connection(self) :
        return self.connection
    
    def get_cursor(self) :
        return self.cursor


    def close(self) :
        try :
            self.get_connection().close()
            print("Connection closed !")
        except psycopg2.Error as e:
            print("Error while closing the connection :", e)

    def commit(self) :
        try :
            self.get_connection().commit()
            print("Commit successful !")
        except psycopg2.Error as e:
            print("Error while commiting :", e)

    def execute(self, sql_request) :
        try :
            self.get_cursor().execute(sql_request)
            print("Request successfully executed !")
        except psycopg2.Error as e:
            print("Error while executing the request :", e)

    def execute_and_print_results(self, sql_request) :
        try :
            self.get_cursor().execute(sql_request)
            results = self.get_cursor().fetchall()
            for row in results :
                print(row)
            print("Request successfully executed !")
        except psycopg2.Error as e:
            print("Error while executing the request :", e)