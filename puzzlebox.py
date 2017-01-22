import random


class Puzzlebox(object):
    """Puzzlebox for codewars kata."""

    def __init__(self):
        self.key = random.randint(1, 99)

    answer = "Ha, not quite that easy.\n"

    hint = "How do you normally unlock things?\n"

    hint_two = "The lock attribute is a method. Have you called it with anything yet?\n"

    def lock(self, *args):
        if len(args) != 1:
            return "This method expects one argument.\n"
        elif type(args[0]) != int:
            return "This method expects an integer.\n"
        elif args[0] != self.key:
            return "Did you know the key changes each time you print it?\n"
        else:
            return "You put the key in the lock! The answer is, of course, 42. Return that number from your answer() function to pass this kata.\n"

    def __repr__(self):
        return "The built-in dir() function is useful. Continue adding print statements till you know the answer.\n"

puzzlebox = Puzzlebox()
