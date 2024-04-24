# File: TMReward.py

"""This module defines a class to represent a single reward."""

class TMReward:

    def __init__(self, text, multiplier):
        """Creates a new TMReward object with these attributes."""
        self._text = text
        self._mult = multiplier

    def get_text(self):
        """Returns the text of this reward."""
        return self._text

    def get_multiplier(self):
        """Returns the multiplier for this reward type"""
        return self._mult


def read_reward(f):
    """Reads the next TMReward, returning None at the end."""

    text = f.readline().rstrip()             # Read the reward name
    if text == "":                           # Returning None at the end
        return None

    multiplier = float(f.readline().rstrip())

    return TMReward(text, multiplier)  # Return the completed object
