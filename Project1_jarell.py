names=("Alice", "Bob", "Charlie", "David")
scores=(85, 92, 78, 90)
alternating = []
final = []
for i in range(len(names)):
    final.append(names[i])
    final.append(scores[i])
print(final)

