import sys

# Add the parent directory containing the util directory to the system path
sys.path.append(
    "C:/Users/sai ganesh/OneDrive/Desktop/Hexaware_Training_Project/Case_study"
)

# Import the DBConnUtil from the util package
from util.db_conn_util import DBConnUtil


def test_db_connection():
    try:
        connection = DBConnUtil.get_connection()
        print("Connection successful")
        connection.close()
    except Exception as e:
        print("Failed to connect to database:", e)


if __name__ == "__main__":
    test_db_connection()
