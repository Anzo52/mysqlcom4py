import dbconnector

def custom_q():
    db, cursor = dbconnector.dbconnect()
    print("Enter SQL query")
    myq = input()
    cursor.execute(f"{myq}")
    result = cursor.fetchall()
    # TODO: check if myq is INSERT, UPDATE, or DELETE statement and call db.commit() if so
    db.close()
    print(result)
    return result

if __name__ == "__main__":
    custom_q()