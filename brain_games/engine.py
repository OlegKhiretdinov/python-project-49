from brain_games.cli import welcome_user, get_answer_for_question


ROUND_COUNT = 3


def engine(game_description, round):
    name = welcome_user()
    print(game_description)

    for _ in range(ROUND_COUNT):
        (correct_answer, question) = round()
        user_answer = get_answer_for_question(question)
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f'\'{user_answer}\' is wrong answer ;('
                  f'. Correct answer was \'{correct_answer}\'.\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
