#file folder1_one.py

"""
This Python script demonstrates a biased selection of people based on their ratings.
The selection is achieved through weighted random sampling, where each person's
probability of being chosen is proportional to their rating.

Attributes:
    people (list of dicts): A list of people with their corresponding ratings.

Functions:
    biased_selection(people): Selects a person from the list based on their rating with biased weighting.

Example:
    >>> selected_person = biased_selection(people)
    >>> print("Selected person:", selected_person["name"])
"""

import random

# List of people and their ratings
people = [
    {"name": "Alice", "rating": 10},
    {"name": "Bob", "rating": 5},
    {"name": "Charlie", "rating": 2},
    {"name": "Diana", "rating": 8},
    {"name": "Eve", "rating": 7},
]

# Function to select a person based on biased weighting
def biased_selection(people):
    """
    Selects a person from the given list with a bias toward higher ratings.
    Each person's chance of being selected is proportional to their rating.
    
    Args:
        people (list of dict): List of people with their ratings.

    Returns:
        dict: The selected person.
    """
    # Calculate the total rating for weighted probabilities
    total_rating = sum(person["rating"] for person in people)

    # Create a list of cumulative probabilities
    cumulative_probabilities = []
    cumulative = 0
    for person in people:
        # Compute the cumulative probability for each person
        cumulative += person["rating"] / total_rating
        cumulative_probabilities.append(cumulative)

    # Generate a random number to determine the selection
    rand = random.random()  # Generates a number between 0 and 1
    for i, cumulative_prob in enumerate(cumulative_probabilities):
        if rand < cumulative_prob:
            return people[i]

# Select one person with biased weighting
selected_person = biased_selection(people)
print("Selected person:", selected_person["name"])
