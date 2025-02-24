# This function prints the multiplication table of a given number.
def table(a):
    for i in range(1, 11):
        print(f"{a} * {i} = {a*i}")

# This function tells wheather a year is leap year or not.
def leap_year(a):
    if(a%100==0):
        if (a % 400 == 0):  # 100,400
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        if(a % 4==0 ): #100,400
            print("Leap Year")
        else:
            print("Not Leap Year")

# This function prints wheather a number is prime or not.
def prime(a):
    ans = "Prime"
    for i in range(2, a):

        if(a%i==0):
            ans="Not prime"
    print(ans)

# This function prints True for a armstorm number and false otherwise.
def armstrom(a):
    sum=0
    temp=a
    while(a>=1):
        x = a % 10
        sum += x**3
        a=int(a/10)
    if(sum == temp):
        print("True")
    else:
        print("False")

# This function returns the factorial of a given number
def fact(a):
    fact=1
    for i in range(1, a+1):
        fact=fact*i
    return fact

# Prints "True" for even and "False" for odd numbers
def odd_even(a):
    print(a%2==0)

# Prints "True" for palindrome "False" otherwise.
def palindrome(a):
    temp=a
    x=0
    while(a>=1):
        x+=a%10
        x*=10
        a=int(a/10)
    print(x/10==temp)


# Prints fibonacci numbers upto a given value
def fibo(a):
    sum=1
    sum_prev=0
    temp=0
    print(sum_prev)
    print(sum)
    for i in range(1, a):
        temp=sum
        sum=sum+sum_prev
        sum_prev=temp
        print(sum)