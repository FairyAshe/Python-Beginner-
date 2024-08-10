#Basic variables is used to store data types

firstname = "Ashe" #string
lastname = "Fernandez" #string
age = 18 #integer
money = 250.5 #float
isTall = False #boolean

#print is used to print something on the screen

print("Hi! my name is, " + firstname + " " + lastname)
print(age)
print(money)
print(isTall)

#input() is used to input something on the console

firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
print("Hi! welcome to Python, " + firstname + " " + lastname)
age = input("How old are you?: ")
print("You are " + age + ", Great")

#Casting variables is a technique use to convert data type to another data type
#str(number) is used to convert NUMBERS INTO STRING
#int(string) AND float(string) is used to convert STRINGS INTO NUMBERS

money = "300"
sunscreen = 199
# print(money - sunscreen) will be an error because they don't have the same data type
print(int(money) - sunscreen) #We used CASTING to convert the STRING INTO INTEGER para mag work
moneys = "300"
sunscreens = 199
print(money + " " + str(sunscreen))