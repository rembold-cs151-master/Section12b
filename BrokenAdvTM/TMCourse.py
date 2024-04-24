# File: TMCourse.py

"""This module defines a class to represent a TeachingMachine course."""

# Implementation notes: TMCourse
# ------------------------------
# The data file for a course consists of questions, each of which has
# the following format:
#
#     Name of the question (a single line)
#     The text of the question (one or more lines)
#     -----
#     Lines for the answers in the form <answer>:<next-question>

from TMQuestion import read_question
from TMReward import read_reward
from random import choice

class TMCourse:

    def __init__(self, questions):
        """Creates a new TMCourse object with the specified questions."""
        self._questions = questions

        # Read in rewards
        with open('rewards.txt') as rf:
            self._possible_rewards = []
            finished = False
            while not finished:
                reward = read_reward(rf)
                if reward is None:
                    finished = True
                else:
                    self._possible_rewards.append(reward)

        # Randomly distribute rewards to questions
        for reward in self._possible_rewards:
            chosen_question = choice(tuple(self._questions.keys()))
            chosen_question.add_reward(reward)


    def run(self):
        """Steps through the questions in this course."""
        current = "START"
        total_points = 0
        while current != "EXIT":
            question = self._questions[current]
            answers = question.get_answers()
            rewards = question.get_rewards()
            points = 1
            print()
            if rewards:
                print(rewards.get_text())
                points *= rewards.get_multiplier()
            for line in question.get_text():
                print(line)
            response = input("> ").strip().upper()
            next_question = answers.get(response, None)
            correct = True
            if next_question is None:
                next_question = answers.get("*", None)
                correct = False
            if next_question is None:
                print("I don't understand that response.")
            else:
                if correct:
                    print(f"  You earned {points} points!")
                    total_points += points
                current = next_question
        print(f"\nYou earned a total of {total_points} points!")
    
# Implementation notes: read_course
# ---------------------------------
# This method is defined within the TMCourse.py module but outside the
# TMCourse class.  Unlike the other methods in the class, read_course
# is not applied to a TMCourse instance but instead returns a new one.
# To ensure that the program starts with the first question, this function
# stores the reference under the key "START" as well as its name.

def read_course(f):
    """Reads the entire TMCourse from the data file f."""
    questions = { }
    finished = False
    while not finished:
        question = read_question(f)
        if question is None:
            finished = True
        else:
            name = question.get_name()
            if len(questions) == 0:
                questions["START"] = question
            questions[name] = question
    return TMCourse(questions)
