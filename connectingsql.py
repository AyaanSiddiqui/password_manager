import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection




def inserting():
    cursor = mydb.cursor() #Initialising pointer to enter commands
    user = input("Please provide username: ")
    passwd = input("Please provide respective passwd: ")
    website_name = input("Enter website's or app's name:")
    if user=="" or passwd=="":
        print("You have not entered username or password!!")

    else:
        # try:
        insert = "INSERT INTO pass (username,password) VALUES(%s,md5(%s))" #%s --> can be used to replace values
        values = [(user,passwd)]
        cursor.executemany(insert,values)
        insert_web = "INSERT INTO pass (site_or_app) VALUES(%s)"
        cursor.execute(insert_web, website_name)
        mydb.commit()
        print(cursor.rowcount, "was inserted.")
        # except:
        #     # 
        #     pass
inserting()
def reading():
    cursor = mydb.cursor() #Initialising pointer to enter commands
