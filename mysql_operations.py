import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Configure logging
logging.basicConfig(
    filename="dboperations.log",         # Log file name
    level=logging.INFO,              # Minimum log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Time + Level + Message
    datefmt="%Y-%m-%d %H:%M:%S",     # Timestamp format
    filemode="w"                     # Overwrite file each run
)

#varible
dbinfo = "MySQL"

#class
class DBOperations:
    def __init__(self):
        try:
            host = os.getenv("MYSQL_HOST")
            user = os.getenv("MYSQL_USER")
            password = os.getenv("MYSQL_PASSWORD")
            database = os.getenv("MYSQL_DATABASE")

            if not all([host, user, password, database]):
                raise ValueError("One or more required DB environment variables are missing.")

            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            logging.info("Database connection established successfully.")

        except Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise
        except Exception as ex:
            logging.error(f"Unexpected error: {ex}")
            raise
    def getall_databases(self):
        try:
            logging.info("Fetching all databases...")
            self.cursor.execute("SHOW DATABASES")
            dbs = self.cursor.fetchall()
            for db in dbs:
                print(db)
            logging.info("Databases fetched successfully.")
        except Error as e:
            logging.error(f"Error fetching databases: {e}")

    def create_tbl(self,tblname,clms):
        try:
            logging.info("Fetching all databases...")
            create_ste =("""CREATE TABLE IF NOT EXISTS {} ({}   VARCHAR(10) PRIMARY KEY, {}  VARCHAR(100) NOT NULL,{} INT,{}   VARCHAR(50),create_ts    TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),created_by   VARCHAR(50) DEFAULT "VIGNESH_KUMAR_R")
                        """).format(tblname,clms[0],clms[1],clms[2],clms[3])
            print("create_ste:",create_ste)
            logging.info(f"create_ste:{create_ste}")
            self.cursor.execute(create_ste)
            tblc = self.cursor.fetchall()
            print(tblc)
            logging.info(f"Table {tblname} created successfully.")
        except Error as e:
            logging.error(f"Error creating table: {e}")
    def insert_tbl(self,cust_data):
        try:
            logging.info("inserting into tblcustomer_vignesh...")
            insert_sql = """
            INSERT INTO tblcustomer_vignesh (custid, fullname, age, profession)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.executemany(insert_sql,cust_data)
            self.conn.commit()
            logging.info(f"Inserted {self.cursor.rowcount} tblcustomer_vignesh records successfully.")
        except Error as e:
            logging.error(f"Error creating table: {e}")
    def execute_query(self, query, params=None):
        try:
            logging.info(f"Executing query: {query}")
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            logging.info("Query executed successfully.")
            return results
        except Error as e:
            logging.error(f"Error executing query: {e}")