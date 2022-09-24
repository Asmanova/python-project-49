import prompt
from random import randint


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_number():
    number = randint(1, 100)
    print(f'Question: {number}')
    return number


def get_answer():
    answer = prompt.string('Your answer: ').lower()
    return answer


def is_winner(number, answer):
    if answer == is_even(number):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{is_even(number)}'")
        return False


def make_game():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_correct = 0
    max_count_correct = 3
    while count_correct < max_count_correct:
        random_number = get_number()
        user_answer = get_answer()
        if is_winner(random_number, user_answer):
            count_correct += 1
        else:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
