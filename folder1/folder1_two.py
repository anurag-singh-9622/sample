# folder1_two.py

import random

# Creating a list of 50 players with varying performance ratings
players = [{"name": f"Player {i + 1}", "performance": random.randint(1, 100)} for i in range(50)]

# Function to select players based on biased weighting
def biased_selection(players, num_to_select):
    """
    Selects a specified number of players from a list with a bias toward higher performance ratings.
    Each player's chance of being selected is proportional to their performance rating.
    
    Args:
        players (list of dict): List of players with their performance ratings.
        num_to_select (int): Number of players to select.

    Returns:
        list of dict: The list of selected players.
    """
    # Calculate the total performance rating for weighted probabilities
    total_performance = sum(player["performance"] for player in players)

    # Create a list of cumulative probabilities
    cumulative_probabilities = []
    cumulative = 0
    for player in players:
        cumulative += player["performance"] / total_performance
        cumulative_probabilities.append(cumulative)

    # Select players based on the cumulative probabilities
    selected_players = []
    for _ in range(num_to_select):
        rand = random.random()
        for i, cumulative_prob in enumerate(cumulative_probabilities):
            if rand < cumulative_prob:
                selected_players.append(players[i])
                break

    return selected_players

# Define the number of players to select for the cricket team (e.g., 11 for a typical team)
num_players_to_select = 11

# Select the players for the cricket team
selected_players = biased_selection(players, num_players_to_select)

# Output the selected players
print("Selected players for the cricket team:")
for player in selected_players:
    print(f"{player['name']} - Performance: {player['performance']}")
