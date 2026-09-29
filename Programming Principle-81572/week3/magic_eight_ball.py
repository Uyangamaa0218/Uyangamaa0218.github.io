import random

RESPONSES = [
    "It is certain.",
    "Without a doubt.",
    "Most likely.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "My reply is no.",
    "Very doubtful."
]
def get_eight_ball_response():
    return random.choice(RESPONSES) 
