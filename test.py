import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection




def inserting():
    cursor = mydb.cursor() #Initialising pointer to enter commands
    user = input("Enter username: ")
    passwd = input("Enter passwd: ")
    if user=="" or passwd=="":
        print("You have not entered username or password!!")

    else:
        try:
            insert = "INSERT INTO pass (username,password) VALUES(%s,md5(%s))" #%s --> can be used to replace values
            values = [(user,passwd)]
            cursor.executemany(insert,values)
            mydb.commit()
            print(cursor.rowcount, "was inserted.")
        except:
            print("No such table is present. Please modify you sql query in code. ")
