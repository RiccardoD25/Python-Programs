dog_name = "Benny"
print(f"My dog's name is {dog_name}. {dog_name} is cute") #calls out dog name and easy to edit name 



#calls out my name in title case. There is also .upper() and .lower() for changing to ipper and lower case
my_name = "Riccardo"
print(f"hi there, my name is {my_name}. nice to meet you.".title()) 



#calls out my name : (Hello Riccardo)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Riccardo")



def describe_yourself(name, age):
        print(f"My name is {name}. My age is {age}") #calls out my name and age

describe_yourself("Riccardo", 32)



def pizza_name(topping):
    print(f"{topping.title()} Pizza") # calls out the pizza topping and in title case

pizza_name("pepperoni")



def times_two(num):
    return num * 23 #Multiplies by 2

print(times_two(2))



numbers = [1, 2, 3]
pizza_toppings = ["cheese", "pepperoni"]
list_of_lists = [[1, 2], [2, 3]]


pizza_toppings.append("pineapple") #adds another topping to the list
pizza_toppings.insert(0, "mushrooms")#puts this topping as first on the list
print(pizza_toppings)



del pizza_toppings[0] #we can also delete toppings from the index
print(pizza_toppings)



pizza_toppings.pop()
print(pizza_toppings) #remove items from the end of the list. brings it back to original toppings



pizza_toppings.remove("cheese") #removes the topping cheese. Will remvove only the first instance
print(pizza_toppings)



pizza_toppings = ["cheese", "cheese", "pepperoni"]
pizza_toppings.remove("cheese")
print(pizza_toppings)#only 1 cheese pizza was removed not both on the list



#how to use a loop
pizza_toppings = ["cheese", "pepperoni", "mushroom"]
for my_topping in pizza_toppings:
    message = f"I would like {my_topping} on my pizza"
    print(message)



#loop every element in my_numbers and store it in my_square_numbers
my_numbers = [1, 2, 3]
my_square_numbers = []
for number in my_numbers:
    my_square_numbers.append(number**2)
print(my_square_numbers)


#runs the numbers in list down sequence
for i in [1, 2, 3, 4, 5]:
    print(i)


#range outputs all numbers quicker. Remember the off by one rule in computers
for i in range(1, 11):
    print(i)

#Another way to output list of numbers
print(list(range(1, 11)))


#prints out numbers greater tahn 5 Boolean effect style
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_greater_than_five = []

for i in numbers:
    if i > 5:
        numbers_greater_than_five.append(i)
print(numbers_greater_than_five)



#If-else statements with additonal fees 
pizza_toppings = ["cheese", "pepperoni"]
print("We have the following toppings:")
for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping} (free)")
    else:
        print(f"{topping} ($1.00)")




#Expected output
#Welcome to Juli'es Pixxeria
#Our available toppings are:
#Cheese (Free)
#Pepperoni ($1.00)
pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1.00)"
    
def print_menu(toppings):
    print("Welcome to Julie's Pizzeria")
    print("Our available toppings are")
    for topping in toppings:
        print(format_topping(topping))
print_menu(pizza_toppings)




#Importing turlte
import turtle

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Lines Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")
my_turtle.forward(100)

for x in range(0,8):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.left(45)
    
my_turtle.hideturtle()
turtle.done()




