import prompt


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    answer = prompt.string('Your answer: ').lower()
    return answer


def is_winner(correct_answer, user_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        return False


max_count_correct = 3
