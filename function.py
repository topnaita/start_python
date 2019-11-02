#how to create out own function


def hello(): #def mean this gonna ba a funcion
    print("hello world")


hello()#I'm calling the function to work. without space.

#another example

def hello (name):
    print("Hello" + name)

hello("jose")
hello("ryan")

#another example. 
def hello (name = "person"): #if there no name, "person" gonna be the default key
    print("Hello" + name)

hello("jose")
hello("ryan")
hello()#if you don't send any value  user (name = "person")


#another example


def add (n1, n2):
    return n1 + n2

print (add(10, 52))
print (add(522, 654))


#FUNCTIONS lambda 

add = lambda number_one, number_two: nomnumber_one + number_two #this is another way of using function in one line 
#it say take two number and sum the quantity.

print(add(10, 87))