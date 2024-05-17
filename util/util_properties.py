import configparser


class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        config = configparser.ConfigParser()
        config.read("db.properties")
        connection_string = (
            f"DRIVER={config['database']['driver']};"
            f"SERVER={config['database']['server']};"
            f"DATABASE={config['database']['database']};"
        )
        return connection_string
