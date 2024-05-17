import pyodbc


class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            driver = "SQL Server"
            server = "SaiGanesh"
            database = "CarRentalSystem"

            connection_string = (
                f"DRIVER={driver};" f"SERVER={server};" f"DATABASE={database};"
            )

            DBConnUtil.connection = pyodbc.connect(connection_string)
        return DBConnUtil.connection
