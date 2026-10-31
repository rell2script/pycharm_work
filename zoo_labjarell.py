import random

zoo = {
    "Savanna": ["Lion", "Giraffe", "Zebra"],
    "Jungle": ["Monkey", "Tiger", "Parrot"],
    "Aquarium": ["Shark", "Dolphin", "Turtle"],
    "Arctic": ["Polar Bear", "Penguin", "Seal"],
}

visitor_counts = {}
for exhibit in zoo:
    visitor_counts[exhibit] = random.randint(10, 100)

print("ZOO EXHIBIT REPORT")
print("------------------")
for exhibit in zoo:
    print(f"Exhibit: {exhibit}")
    print(f"Animals: {zoo[exhibit]}")
    print(f"Visitors: {visitor_counts[exhibit]}")

# Add the counts with a loop
total_visitors = 0
for exhibit in visitor_counts:
    total_visitors += visitor_counts[exhibit]
print(f"Total visitors: {total_visitors}")

most_visited_exhibit = ""
for exhibit in visitor_counts:
    if not most_visited_exhibit or visitor_counts[exhibit] > visitor_counts[most_visited_exhibit]:
        most_visited_exhibit = exhibit

print(f"Most visited exhibit: {most_visited_exhibit}")
print(f"Number of visitors: {visitor_counts[most_visited_exhibit]}")