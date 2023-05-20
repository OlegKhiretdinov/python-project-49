import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}')
    return name


def get_answer_for_question(question):
    print(f'Question: {question}')
    return prompt.string("Your answer: ")
