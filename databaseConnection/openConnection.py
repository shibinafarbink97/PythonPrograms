import mysql.connector
def getConnection():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwrd = "Password@123",
        database = "COMPANY"
    )
    return db()