from DbConnectPython.openConnection import *
cursor = db.cursor()
query = """"INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('vijay','karan',21,'M',7000)"""
try:
    cursor.execute(query)
    db.commit()
    print("db")
except Exception as e:
    print(e.args)
    db.rollback()
db.close()