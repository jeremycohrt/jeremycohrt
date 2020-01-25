import random
game_over, game, guess_limit = False, None, 0


def mastermind(code):
    guesses = 0

    def num_to_list(num):
        result = []
        while num:
            result = [num % 10] + result
            num //= 10
        return result

    def repeat_check(guess):
        for i in range(len(guess)):
            for j in range(i + 1, len(guess)):
                assert guess[i] != guess[j]

    original_code, code = code, num_to_list(code)

    def game(guess):
        global game_over, guess_limit
        nonlocal guesses
        guess = num_to_list(guess)

        try:
            assert len(code) == len(guess)
        except AssertionError:
            return print("Incorrect guess length. The correct length is {0}.".format(str(len(code))))
        try:
            repeat_check(guess)
        except AssertionError:
            return print("No repeats.")

        guesses += 1
        i, correct_position, incorrect_position = 0, 0, 0

        while i < len(code):
            if guess[i] == code[i]:
                correct_position += 1
            elif guess[i] in code:
                incorrect_position += 1
            i += 1

        if correct_position == len(code):
            game_over = True
            if guesses == 1:
                return print("You lucky bastard!" + "\n")
            print("You won with " + str(guesses) + " guesses!" + "\n")
        else:
            print("You had {0} in the correct position and {1} in the incorrect position.".format(str(correct_position), str(incorrect_position)))

        if guesses >= guess_limit:
            game_over = True
            return print("You have reached the maximum amount of guesses. The code was {0}.".format(original_code) + "\n")

    try:
        repeat_check(code)
    except AssertionError:
        return print("No repeats.")
    return game


def code_randomizer(digit_limit, code_limit):
    numbers, code, i = list(range(1, digit_limit + 1)), 0, 0
    while i < code_limit:
        current = random.choice(numbers)
        code += (current * pow(10, i))
        i += 1
        numbers.remove(current)
    return code


def start_game():
    global game_over, guess_limit
    game_over = False
    digit_limit, code_limit, guess_limit = 0, 0, 0

    while not guess_limit:
        try:
            guess_limit = input("How many guess attempts do you want to have? ")
            guess_limit = int(guess_limit)
            assert guess_limit > 0
        except AssertionError:
            print("They say the sky's the limit, but not in this game. Make sure your guess limit is above 0.")
            guess_limit = 0
    while not digit_limit:
        try:
            digit_limit = input("How many possible digits do you want to play with? ")
            digit_limit = int(digit_limit)
            assert digit_limit < 10 and digit_limit > 0
        except AssertionError:
            print("They say the sky's the limit, but not in this game. Make sure your digits are between 1 and 9.")
            digit_limit = 0
    while not code_limit:
        try:
            code_limit = input("How long do you want the code to be? ")
            code_limit = int(code_limit)
            assert code_limit < 10 and code_limit > 0 and code_limit <= digit_limit
        except AssertionError:
            print("They say the sky's the limit, but not in this game. Make sure your code length is between 1 and 9.")
            code_limit = 0
    print("Have fun!" + "\n")
    game = mastermind(code_randomizer(digit_limit, code_limit))

    while not game_over:
        guess = input("Guess a number. ")
        game(int(guess))


while True:
    start_game()
