from brain_games.cli import welcome_user, get_answer_for_question


def engine(welcome_txt, round):
    name = welcome_user()
    print(welcome_txt)

    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        (correct_answer, question) = round()
        user_answer = get_answer_for_question(question)
        if user_answer == str(correct_answer):
            print("Correct!")
            win_count += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;('
                  f'. Correct answer was \'{correct_answer}\'.')
            loose_count += 1

    if win_count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
