import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="ILOVEcoding", database="userandpass") #Establishing connection
cursor = mydb.cursor(buffered=True) #Initialising pointer to enter commands




def inserting():
    user = input("Please provide username: ")
    passwd = input("Please provide respective passwd: ")
    website_name = input("Enter website's or app's name:")

    if user=="" or passwd=="":
        print("You have not entered username or password!!")

    else:
        try:
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
        except Exception as e:
            print("SOMETHING WENT WRONG....PLEASE TRY AGAIN\n",e)

        finally:
            with open("G:\cracking\wordlists.txt","a") as f:
                f.write(passwd)


def displaying():
    try:
        print("\nPlease provide name of app or site or username to find password:")
        app_name=input()
        cursor.execute("SELECT password from pass WHERE site_or_app='"+app_name+"' or site_or_app='"+app_name+"'")
        reading_result = cursor.fetchall()
        print("\nYour result hash is:\n")
        for i in reading_result:
            tuple_pointer = i
            print(tuple_pointer[0])
    except Exception as e:
        print("\nPlease provide correct name.\n",e)
        


def displaying_websites():
    cursor.execute("SELECT site_or_app from pass")
    sites_list=cursor.fetchall()

    for result in sites_list:
        result_pointer = result
        print(result_pointer[0])



def create_table():
    try:
        cursor.execute("CREATE TABLE  pass (id int NOT NULL AUTO_INCREMENT,username VARCHAR(100),password VARCHAR(40),site_or_app VARCHAR(100),PRIMARY KEY (id))")
        print("\nTable successfully created\n")
    except Exception as e:
        print(e)



# if __name__=="__main__":
    # inserting()
    # create_table()
    # displaying_websites()
    # displaying()
    print("")