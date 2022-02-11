from connectingsql import inserting, displaying,displaying_websites,create_table

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Save new password')
    print('2. Find a password for a site or app')
    print("3. Display all apps and websites")
    print('4. Create table if not present')
    print('Q. Exit')
    print('-'*30)
    return input(": ")

choice=menu()

while choice!="Q":
    if choice=="1":
        inserting()
    if choice=="2":
        displaying()
    if choice=="3":
        displaying_websites()
    if choice=="4":
        create_table()
    if choice!="1" or choice!="2" or choice!="3" or choice!="4":
        choice=menu()
        
exit()