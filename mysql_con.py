from dotenv import load_dotenv
import os
import mysql.connector
import logging

import logging

# Configure logging
logging.basicConfig(
    filename="logging.log",         # Log file name
    level=logging.INFO,              # Minimum log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Time + Level + Message
    datefmt="%Y-%m-%d %H:%M:%S",     # Timestamp format
    filemode="w"                     # Overwrite file each run
)

# Load environment variables from .env
load_dotenv()

# Read MySQL config
config = {
    'host': os.getenv('MYSQL_HOST'),
    'port': int(os.getenv('MYSQL_PORT')),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

# Connect and run query
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("SHOW DATABASES;")  # Sample query
    result = cursor.fetchone()
    logging.info(f"Connected to DB: {result}")
    
except mysql.connector.Error as err:
    logging.error(f"Error: {err}")
finally:
    if conn:
        conn.close()
    if cursor:
        cursor.close()
