from prettytable import PrettyTable
import ast
data_path='D:/work_space/BCT_2025/BCT_django_2025/Day-2/login_interface/data.txt'  #Change according to your need.
def load_data():
    data=[]
    
    with open(data_path, 'r') as mf:
        l=mf.read().split(';')
        l.pop()
        for u in l:
            u=u.strip('{')
            u=u.strip('}')
            u=u.replace("'", "")
            res = []
            for sub in u.split(', '):
                if ':' in sub: 
                    res.append(map(str.strip, sub.split(':', 1)))
            user = dict(res)
            data.append(user)
    return data

current_user={}

def isLoggedIn():
    for user in current_user:
        if user:
            return True
        return False


def logOut():
    current_user.clear()
    current_user.update({})
    print("Logged out successfully.")

def getCurrentUser():
    myTable = PrettyTable(["Email", "Password"])
    myTable.add_row([current_user["email"] , current_user["password"]])
    return myTable


def signIn():
    l=[]
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    l=load_data()
    for user in l:
        if user['email']==email:
            if(user['password']==password):
                current_user.clear()
                print(user)
                current_user.update(user)
                print("Login successfull.")
                return
            else:
                print("Incorrect password.")
                return
    print(f"{email} is not registered, signup first.")
    

        
        

def signUp():
    database = {}
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    if(email.endswith(".com")):
        database["email"] = email
        database["password"] = password
        s=str(database)+";"
        file1 = open(data_path, "a")
        file1.write(s)
        file1.close()
        print("Signup successfull.")
        return
    print("Enter a valid email: ")
    

def showAllData():
    l=load_data()
    myTable = PrettyTable(["no.", "Email", "Password"])
    n=1
    for user in l:
        
        myTable.add_row([n, user["email"] , user["password"]])
        n+=1
    
    return myTable 