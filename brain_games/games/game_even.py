import brain_games.games.common as common
from random import randint
import brain_games.main as main


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_question():
    return randint(1, 100)


def game_even():
    user_name = main.user_name

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct = 0
    while count_correct < common.max_count_correct:
        question = get_question()
        common.ask_question(question)

        user_answer = common.get_answer()
        correct_answer = is_even(question)

        if common.is_winner(correct_answer, user_answer):
            count_correct += 1
        else:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
