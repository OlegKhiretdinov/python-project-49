from brain_games.cli import welcome_user, get_answer_for_question
from brain_games.utils.utils import get_is_answer_correct, finish_game


def engine(welcome_txt, round):
    name = welcome_user()
    print(welcome_txt)

    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        (correct_answer, question) = round()
        user_answer = get_answer_for_question(question)
        is_correct = get_is_answer_correct(user_answer, str(correct_answer))

        if is_correct:
            win_count += 1
        else:
            loose_count += 1

    finish_game(win_count == 3, name)
