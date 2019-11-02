foods = [ 'apples', 'bread', 'cheese', 'milk', 'graves']

#using for you can add item automaticaly with no issue.
for food in foods: # for food "variable" in list foods print food
    print(food)

#another example. see below

for food in foods:
    if food == 'cheese': #this replace cheese for the string you see below.
        print('you need to buy this.')

#another example.

for food in foods:
    if food == 'cheese': #this replace cheese for the string you see below.
        break #this break and end it up at cheese.
    print(food)


#another example.

for number in range(1, 20): #show range of numbre 
    print ()

#another example.

for letter in "hello":
    print(letter)


#LOOP WHILE example
count = 1

while count <= 10:
    print(count)
    count = count + 1 

