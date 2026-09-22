#question1
movies=["Superbad","Friday","Titanic","Sinners","Obsession"]
movies.append("Superman")
movies.append("Superwoman")
movies[2]="The matrix"
print(movies[0])
print(movies[-1])
movie_total=len(movies)
print(movie_total)
for movie in movies:
    print(movie)
fav_movies=(movies[0:3])
print(fav_movies)


#question2
pizzas=["Pepperoni","Mushroom","Cheese"]
for pizza in pizzas:
    print (f"I like {pizza} pizza! ")
print("I love pizza!")

#question3
food=("Rice","Chicken","Potato","Beef","Carrots")
for foods in food:
    #print(f"We have {food} here!")
#[2]=("Mayo")
food=("Brown rice","Turkey","Potato","Beef","Carrots")
for new_foods in food:
    print(f"We now have {food} here!")