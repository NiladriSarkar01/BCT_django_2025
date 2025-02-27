from login_interface import signIn, signUp, showAllData, logOut, getCurrentUser, isLoggedIn

def main():
    while True:
        print('''\n0.Exit.\n1.Signup.\n2.Signin.\n3.See all data(login required.)\n4.Logout.\n5.Get current user.''')
        
        key=input("\n>>>")
        if(key=='0'):
            break
        elif(key=='1'):
            if(isLoggedIn()):
                print("Logout first to create a new account.")
            else:
                signUp()
        elif(key=='2'):
            if(isLoggedIn()):
                print("You are already logged in.")
            else:
                signIn()
        elif(key=='3'):
            print(isLoggedIn())
            if(isLoggedIn()):
                print(showAllData())
            else:
                print("Login first.")
        elif(key=='4'):
            if(isLoggedIn()):
                logOut()
            else:
                print("You are already logged out.")
        elif(key=='5'):
            if(isLoggedIn()):
                print(getCurrentUser())
            else:
                print("No user is currently logged in.")
        else:
            print("Please enter a valid parameter.")

if __name__== "__main__":
    main()