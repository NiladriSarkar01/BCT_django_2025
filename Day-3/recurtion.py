def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def sumOfNnumbers(n):
    if n==1:
        return 1
    return n+sum(n-1)

def main():
    n=int(input("Enter a number: "))
    print(f"Sum of natural numbers till {n} is {sumOfNnumbers(n)}")
    b=int(input("Enter a number: "))
    print(f"factorial of {b} is {factorial(b)}")

if __name__=="__main__":
    main()