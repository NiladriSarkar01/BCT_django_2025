factorial=lambda a:1 if(a<=1) else (a*factorial(a-1))

sum=(lambda a: 1 if a==1 else (a+sum(a-1)))

a=(lambda a, b:a+b)(12, 45)

def main():
    print(factorial(int(input())))
    print(sum(int(input())))
    print(a)

if __name__=="__main__":
    main()
