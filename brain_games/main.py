import prompt


def introduction():
    print('Welcome to the Brain Games!')
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


user_name = ''
