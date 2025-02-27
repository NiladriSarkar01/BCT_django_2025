from calculator.calculator import multiplication, addition, substraction, division

def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=input("Enter the operator: ")
    ans=0
    if( c == '+' ):
        ans+=addition(a, b)
    elif(c=='-'):
        ans+=substraction(a, b)
    elif(c=='*'):
        ans+=multiplication(a, b)
    elif(c=='/'):
        ans+=division(a, b)
    else:
        print("Please Enter a vslid parameter.")
        return
    print(f"{a} {c} {b} = {ans}")

if __name__ == "__main__":
    main()