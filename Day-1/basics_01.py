# Variables in python

a = 5 #int
str = "hello" #String
tpl = (3, 5, 9) #tuple
dict = {"hello": "world",
     "hdbs": "syd"} #dict
l = [3, 4, 5, 6, 7] #list
set={3, 4, 5, 6, 7} #set

print(type(a))
print(type(str))
print(type(tpl))
print(type(dict))
print(type(l))
print(type(set))

# type casting (tuple to list)
ls=list(tpl)
print(type(ls))


# appending a value in the list
ls.append(input("Enter the value"))
# type casting (list to tuple)
tpl=tuple(ls)
print(tpl)
print(type(tpl))

# appending to tuples
tpl=tpl+(5, 6)
print(tpl)


# swaping 2 variables
a = 6
b = 7
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")
