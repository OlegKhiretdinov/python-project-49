def get_is_answer_correct(user_val, correct_val):
    if user_val == correct_val:
        print("Correct!")
        return True
    else:
        print(f'\'{user_val}\' is wrong answer ;('
              f'. Correct answer was \'{correct_val}\'.')
        return False


def finish_game(is_vin, name):
    if is_vin:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
