
player = "Hero"
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
powerups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]
actions = [0, 1, 0, 2, 1]
action_names = {0: "Collect Coins", 1: "Fight Enemies", 2: "Use Power-Up"}

# A level earns 10 points per coin, loses 5 points per enemy, and gets
# 25 bonus points for a Star. This formula reproduces the provided scores.
level_scores = []
for index in range(len(coins)):
    score = coins[index] * 10 - enemies[index] * 5
    if powerups[index] == "Star":
        score += 25
    level_scores.append(score)

score = 0
score_history = []
for level_score in level_scores:
    score += level_score
    score_history.append(score)

action_results = []
for action in actions:
    if action == 0:
        result = "Collect Coins"
    elif action == 1:
        result = "Fight Enemies"
    else:
        result = "Use Power-Up"
    action_results.append(result)

lives = 3
life_history = []
for index in range(len(coins)):
    if enemies[index] >= 4 and powerups[index] != "Star":
        lives -= 1
    life_history.append(lives)

total_coins = sum(coins)
bonus_coin_levels = [coin for coin in coins if coin >= 7]

inventory = ["Mushroom", "Star", "Flower"]
starting_inventory = inventory.copy()
used_powerups = ["Mushroom", "Star"]
for powerup in used_powerups:
    inventory.remove(powerup)

high_scores = [level_score for level_score in level_scores if level_score >= 50]
total_enemies = sum(enemies)
average_coins = total_coins / len(coins)

print("===== PLATFORM ADVENTURE =====")
for index in range(len(coins)):
    print(f"Level {index + 1}")
    print(f"Coins: {coins[index]}")
    print(f"Enemies: {enemies[index]}")
    print(f"Power-Up: {powerups[index]}")

print("===== PLAYER INFORMATION =====")
print(f"Player: {player}")
print(f"Lives: {3}")
print(f"Score: {0}")
print(f"Total Coins: {0}")

print("===== LEVEL SCORES =====")
for index, level_score in enumerate(level_scores, start=1):
    print(f"Level {index} Score: {level_score}")

print("===== ADVENTURE ACTIONS =====")
for index, result in enumerate(action_results, start=1):
    print(f"Level {index}: {result}")

print("===== LIFE HISTORY =====")
for index, remaining_lives in enumerate(life_history, start=1):
    print(f"After Level {index}: {remaining_lives} lives")

print("===== COIN COLLECTION =====")
print(f"Coins collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

print("===== POWER-UP INVENTORY =====")
print(f"Starting Inventory: {starting_inventory}")
print(f"Used Power-Ups: {used_powerups}")
print(f"Remaining Inventory: {inventory}")

print("===== LEVEL ANALYSIS =====")
print(f"Total Coins: {total_coins}")
print(f"Most Coins in One Level: {max(coins)}")
print(f"Fewest Coins in One Level: {min(coins)}")
print(f"Average Coins per Level: {average_coins:.1f}")
print(f"Total Enemies: {total_enemies}")
print(f"Most Enemies in One Level: {max(enemies)}")

print("===== HIGH SCORES =====")
print(f"Scores of 50 or Higher: {high_scores}")

print("===== SCORE HISTORY =====")
for index, cumulative_score in enumerate(score_history, start=1):
    print(f"After Level {index}: {cumulative_score}")
print(f"First Two Scores: {score_history[:2]}")
print(f"Last Two Scores: {score_history[-2:]}")

print("===== FINAL STATUS =====")
if lives == 0:
    status = "Game Over"
elif score >= 250:
    status = "Adventure Champion"
elif score >= 150:
    status = "Great Adventure"
else:
    status = "Keep Practicing"
print(status)

print("===== ADVENTURE RANKING =====")
print(f"Final Score: {score}")
print(f"Final Lives: {lives}")
if score >= 300:
    rank = "Legend"
elif score >= 200:
    rank = "Expert"
elif score >= 100:
    rank = "Adventurer"
else:
    rank = "Beginner"
print(f"Rank: {rank}")
