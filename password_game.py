class PasswordGame:
    def __init__(self, max_guesses):
        self.password = "1996"
        self.max_guesses = max_guesses

    def play(self):
        print("\n--- Password Guess Game ---")
        print(f"You have {self.max_guesses} attempts to guess the 4-digit password.")

        while self.max_guesses > 0:
            user_guess = input("Guess a password: ")

            if user_guess == self.password:
                print("You got it!")
                break

            else:
                print("Wrong password!")
                self.max_guesses -= 1
                if self.max_guesses > 0:
                    print(f"Attempts left: {self.max_guesses}")
                else:
                    print("You wrong. Game Over.")

