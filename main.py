import random
from art import logo
from art import vs
from game_data import data
import os


# make this as function
# format the account data into printable format
# name = random_data['name']
# follower_count = random_data['follower_count']
# description = random_data['description']
# country = random_data['country']
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def follow_count(account):
    count = account['follower_count']
    return count


def check_answer(guess, count_a, count_b):
    if count_a > count_b:
        # if guess == 'a':
        #   return True
        # else:
        #   return False
        # simply do this a is true
        return guess == 'a'
    else:
        return guess == 'b'


# Display Art
print(logo)
score = 0
account_a = random.choice(data)
account_b = random.choice(data)
game_continue = True
while game_continue:
    # generate a random account
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")

    follower_count_a = follow_count(account_a)
    follower_count_b = follow_count(account_b)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    print(logo)
    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    if is_correct:
        score += 1
        game_continue = True
        print(f"You are right! Your current score is {score}")
    else:
        game_continue = False

        print(f"You are wrong. Your final score is {score}")
