import mysql.connector
import config

def get_config():
    HOST = config.HOST
    USERNAME = config.USERNAME
    PASSWORD = config.PASSWORD
    # DATABASE = config.DATABASE
    # return (HOST, USERNAME, PASSWORD, DATABASE)
    # uncomment 2 lines above and comment out below this line to use DATABASE field
    return (HOST, USERNAME, PASSWORD)

def get_db_cursor(*configs):
    # Connect to the database
    # TODO: checks for "database" and passwd fields (empty or not)
    db = mysql.connector.connect(
        host=configs[0],
        user=configs[1],
        passwd=configs[2],
        database=configs[3]
    )
    # Get the cursor
    cursor = db.cursor()
    return db, cursor

def dbconnect():
    configs = get_config()
    db, cursor = get_db_cursor(configs)
    return db, cursor

if __name__ == "__main__":
    dbconnect()