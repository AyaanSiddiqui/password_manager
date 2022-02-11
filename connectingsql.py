import mysql.connector
import pyperclip

def inserting():
    try:
        mydb=mysql.connector.connect(host="localhost", user="enter_your_user", password="enter_your_sql_pass", database="database_name") #Establishing connection
        cursor = mydb.cursor(buffered=True) #Initialising pointer to enter commands
        user = input("Please provide username: ")
        passwd = input("Please provide respective passwd: ")
        website_name = input("Enter website's or app's name:")
        insert = "INSERT INTO pass (username,password) VALUES(%s,md5(%s))" #%s --> can be used to replace values
        values = [(user,passwd)]
        cursor.executemany(insert,values)
        cursor.execute("SELECT id FROM pass ORDER BY id DESC")
        id_result = cursor.fetchone()
        id_list = []
        for id_no in id_result:
            id_list.append(id_no)
            # print(str(id_list[0]))
        insert_web = "UPDATE pass SET site_or_app=%s WHERE id="+str(id_list[0])
        value_web = [(website_name)]
        cursor.execute(insert_web, value_web)
        mydb.commit()
        print(f"Username '{user}' was inserted")
        print(f"Rows inserted:{cursor.rowcount}")

    except Exception as error:
        print(error)

    finally:
        with open("G:\cracking\wordlists.txt","a") as f:
            f.write(passwd+"\n")

# inserting()

def displaying():
    try:
        mydb=mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection
        cursor = mydb.cursor(buffered=True) #Initialising pointer to enter commands
        print("\nPlease provide name of app or site or username to find password:")
        app_name=input()
        cursor.execute("SELECT password from pass WHERE site_or_app='"+app_name+"' or site_or_app='"+app_name+"'")
        reading_result = cursor.fetchall()
        print("-"*40)
        print("Your result hash is copied to clipboard")
        print("-"*40)
        for i in reading_result:
            tuple_pointer = i
            pyperclip.copy(tuple_pointer[0])

    except Exception as e:
        print("\nPlease provide correct name.\n",e)
        
# displaying()

def displaying_websites():
    try:
        mydb=mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection
        cursor = mydb.cursor(buffered=True) #Initialising pointer to enter commands
        cursor.execute("SELECT site_or_app from pass")
        sites_list=cursor.fetchall()

        for result in sites_list:
            result_pointer = result
            print(result_pointer[0])
    except Exception as e:
        print(e)

# displaying_websites()

def create_table():
    try:
        mydb=mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection
        cursor = mydb.cursor(buffered=True) #Initialising pointer to enter commands
        cursor.execute("CREATE TABLE  pass (id int NOT NULL AUTO_INCREMENT,username VARCHAR(100),password VARCHAR(40),site_or_app VARCHAR(100),PRIMARY KEY (id))")
        print("\nTable successfully created\n")
    except Exception as e:
        print(e)

# create_table()
