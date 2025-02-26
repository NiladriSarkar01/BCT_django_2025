from prettytable import PrettyTable

l = [{"email":"admin", "password":"admin"}]

current_user={"email":"default", "password":"default", "log":False}


def logOut(user):
    for u in l:
        if(u==user):
            u["log"]=False
    print("Logged out successfully.")
    return {"email":"default", "password":"default", "log":False}

def getCurrentUser():
    return current_user


def signIn():

    email=input("Enter your email: ")
    password=input("Enter your password: ")
    n=len(l)
    for user in l:
        if user['email']==email:
            if(user['password']==password):
                print("Login successfull.")
                user["log"]=True
                return user
            else:
                print("Incorrect password.")
                return {"email":"default", "password":"default", "log":False}
    print(f"{email} is not registered, signup first.")
    return {"email":"default", "password":"default", "log":False}
    

        
        

def signUp():
    database = {}
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    if(email.endswith(".com")):
        database["email"] = email
        database["password"] = password
        database["log"]=False
        l.append(database)
        print("Signup successfull.")
    else:
        print("Enter a valid email: ")
    return
    

def showAllData():
    # TODO
    
    myTable = PrettyTable(["no.", "Email", "Password"])
    for user in l:
        n=1
        myTable.add_row([n, user["email"] , user["password"]])
        n+=1
    print(myTable)

def main():
    while True:
        print('''\n0.Exit.
              \n1.Signup.
              \n2.Signin.
              \n3.See all data(login required.)
              \n4.Logout.
              \n5.Get current user.''')
        
        key=int(input("\n>>>"))
        if(key==0):
            break
        elif(key==1):
            signUp()
        elif(key==2):
            current_user.clear()
            current_user.update(signIn())
        elif(key==3):
            if(current_user["log"]):
                showAllData()
            else:
                print("Login first.")
        elif(key==4):
            current_user.clear()
            current_user.update(logOut(current_user))
        elif(key==5):
            print(getCurrentUser())
        else:
            print("Please enter a valid parameter.")

if __name__== "__main__":
    main()