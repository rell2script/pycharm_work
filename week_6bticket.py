# 1.
favorite_numbers = {
    "Rell": 3,
    "Woom": 16,
    "Chloe": 6,
    "Enuel": 21,
    "Emma": 9,
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


# 2.
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Danube": "Germany",
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers:
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)


# 3.
dog = {"kind": "dog", "owner": "Luna"}
cat = {"kind": "cat", "owner": "Nokk"}
rabbit = {"kind": "rabbit", "owner": "Nina"}

pets = [dog, cat, rabbit]

for pet in pets:
    print(f"Kind: {pet['kind']}, Owner: {pet['owner']}")

# Print the first pets information without a loop
print(f"First pet: {pets[0]['kind']}, owned by {pets[0]['owner']}")


# 4.
favorite_places = {
    "Ava": ["Paris", "Tokyo"],
    "Ben": ["the mountains"],
    "Chloe": ["Rome", "New York", "Sydney"],
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: {', '.join(places)}.")


# 5.
movie_ratings = {
    "Spirited Away": 9,
    "The Matrix": 9,
    "Finding Nemo": 8,
    "Jaws": 7,
    "Dune": 8,
}

for movie, rating in movie_ratings.items():
    print(f"{movie}: {rating}")

print("\nMovies rated 8 or higher:")
for movie, rating in movie_ratings.items():
    if rating >= 8:
        print(f"{movie}: {rating}")


# 6.
menu = {
    "soup": 5.50,
    "salad": 7.00,
    "pasta": 12.00,
    "burger": 11.50,
    "pie": 6.00,
}

for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

menu["fries"] = 4.00       # Add an item
menu["pasta"] = 13.00      # Change an existing price

print("\nUpdated menu:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")


# 7.
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "about 14 million",
        "fact": "It has one of the world's busiest train stations.",
    },
    "Cairo": {
        "country": "Egypt",
        "population": "about 10 million",
        "fact": "The city is near the ancient pyramids of Giza.",
    },
    "Lima": {
        "country": "Peru",
        "population": "about 10 million",
        "fact": "It is on the coast of the Pacific Ocean.",
    },
}

for city, information in cities.items():
    print(f"\n{city} is:")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")


# 8. Word Counts
words = ["apple", "banana", "apple", "orange",
         "banana", "apple", "grapes", "orange"]

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


# 9.
courses = {
    "Biology": 24,
    "History": 18,
    "Computer Science": 32,
    "Art": 15,
}

total_students = 0
largest_course = ""
largest_enrollment = 0

for course, enrollment in courses.items():
    print(f"{course}: {enrollment} students")
    total_students += enrollment

    if enrollment > largest_enrollment:
        largest_enrollment = enrollment
        largest_course = course

print(f"Total enrolled students: {total_students}")
print(f"Largest enrollment: {largest_course} ({largest_enrollment} students)")

print("Courses with more than 20 students:")
for course, enrollment in courses.items():
    if enrollment > 20:
        print(f"{course}: {enrollment}")


# 10.
games = {
    "Stardew Valley": {"genre": "simulation", "year": 2016, "rating": 9.0},
    "Minecraft": {"genre": "sandbox", "year": 2011, "rating": 9.5},
    "Fortnite": {"genre": "Fps", "year": 2017, "rating": 9.0},
}

# Add two more games
games["Hades"] = {"genre": "action roguelike", "year": 2020, "rating": 9.0}
games["Apex Legends"] = {"genre": "Fps", "year": 2019, "rating": 9.0}

for game, information in games.items():
    print(f"\n{game}")
    for detail, value in information.items():
        print(f"{detail}: {value}")

print("\nGames rated 9 or higher:")
for game, information in games.items():
    if information["rating"] >= 9:
        print(f"{game}: {information['rating']}")

# Print one game genre and rating without a loop
print(
    f"\nMinecraft is a {games['Minecraft']['genre']} game "
    f"with a rating of {games['Minecraft']['rating']}.")
