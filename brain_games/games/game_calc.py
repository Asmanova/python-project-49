from secrets import choice
import brain_games.games.common as common
from random import randint
import brain_games.main as main


def get_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    addition = (f'{number1} + {number2}', number1 + number2)
    subtraction = (f'{number1} - {number2}', number1 - number2)
    multiplication = (f'{number1} * {number2}', number1 * number2)

    results = [addition, subtraction, multiplication]
    return choice(results)


def game_calc():
    user_name = main.user_name

    print('What is the result of the expression?')

    count_correct = 0
    while count_correct < common.max_count_correct:
        question, correct_answer = get_question()
        common.ask_question(question)

        user_answer = common.get_answer()
        correct_answer = str(correct_answer)

        if common.is_winner(correct_answer, user_answer):
            count_correct += 1
        else:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
