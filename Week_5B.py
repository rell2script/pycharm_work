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

