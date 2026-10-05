#The string "Arnaa" has five characters: the first, second, third, fourth, and fifth character.
#Write a condition that returns whether the second character is "a" AND 3 is less than 5.
name = "Arnaa"
if 3 < 5 and name[1] != "a":
    print ("3 is less than five and Arnaa's second character is not 'a'")

#2
musician= "jcole"
fav_musician= "jcole"
if musician == fav_musician:
    print (f"{musician} is the greatest artist of all time")
else:
    print (f"{musician} is not the greatest artist of all time")

#3
number= -2
if number < 0:
    print (f"{number *-1}")
else:
    print (f"{number}")

#4
professor=("Smith")
cs_professor= False
if cs_professor == True:
    print (f"{professor} is a cs professor")
else:
    print (f"{professor} is not a cs professor")

#5
gpa=4.0
if gpa == 4.0:
    print("You are eligible for the reward")
#Brazil, China, Cabo Verde, Haiti, Portugal
#6
countries= ["Brazil","China","Cabo Verde", "Haiti", "Portugal", "Usa"]
country= "Usa"
if country == countries[0:6]:
    print(f"one of the students in the class was born in {country}")
else:
    print(f"No student from {country} is in this class")

#7 prediction is $12
age = 70
if age<=12:
    print("Pay $5.")
if age > 12 and age < 55:
    print("Pay $12.")
if age >= 55:
    print("Pay $8.")

#8
hours_worked = 41
extra_hours = hours_worked - 40
overtime = extra_hours * 1.5 +hours_worked
if hours_worked <= 40 and hours_worked > 0:
    print(f"before tax:{hours_worked *15}")
if hours_worked >= 40:
    print (f"after tax:{overtime *15}")
if hours_worked < 0:
    print("error")

#9
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#10
word = "mom"
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#11
n = 3
factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(f"{n}! = {factorial}")

#12
#THE error is that the parenthesis is not closed. there also is no "f" in the print statement
fruits = ["apple","banana","mango"]
for i in range(len(fruits)):
    print(fruits[i])
#will pring apple, banana , and mango




#13 code was missing a ":"after the if statement. now will print 6 8 and 10
numbers = [2,6,8,3,10]
for num in numbers:
    if num > 5:
        print(num)

#14 not in checks the list for mike and derek. the names that produce true are John and Sarah
# will print " john can enter. sarah can enter. mike cannot enter. derek cannot enter.
