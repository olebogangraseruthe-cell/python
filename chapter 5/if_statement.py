#Creating only if statements. They do not work together
#Using the variable called temperature with a value equal to 30
temperature = 30

#Statement 1 
if temperature > 25:
    print("If the tep is greater than 25 It is very hot outside")

#Statement 2
if temperature < 40:
    print("If the tep is less than 40 It is just warm outside")

#Statement 3
if temperature == 30:
    print("If the tep is equal to 30 It is just okay outside" , "\n")


#IF-ELSE STATEMENT
color = "red"

if color == "red":
    print("yey the color is red")
else: 
    print("Sorry the color is not red")

#if, elif, else
grade = 35

if grade >= 90:
    print("Passed with A")
elif grade >= 80:
    print("you got a B")
elif grade >= 70:
    print("you got a C")
elif grade >= 60:
    print("you got a D")
else:
    print("You got an F")