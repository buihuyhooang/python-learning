#number = 42
#text = " is this the number?"

#print(str(number) + text)

#print(f"{number}{text}")



number = 42 
text = "{} is this the number?"

print(text.format(number))


my_age = 53
my_wife_age = 47
text = "My age is {1} and my wife's age is {0}"
print(text.format(my_wife_age, my_age))


