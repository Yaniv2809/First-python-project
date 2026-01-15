class MathGame:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self):
        print("Welcome", self.name)
        print("Welcome to the Player Progress Game!")
        print("In this game, the player advances through different levels and completes tasks.")
        print("Each correct task adds points to your score.")
        print("At the end of the game, your total score will be displayed.")
        print("Good luck!\n")


        useranswer = input("What is 3 + 2? ")
        if useranswer == "5" or useranswer.lower() == "five":
            self.score += 10
            print("Correct! +10 points")
        else:
            print("Wrong answer")


        number = int(input("Enter a number greater than 10: "))
        if number > 10:
            self.score += 10
            print("Good job! +10 points")
        else:
            print("Too small")

        userguess = input("Calculate 10/5 = : ")
        if userguess == "2" or userguess.lower() == "two":
            self.score += 20
            print("Amazing! +20 points")
        else:
            print("Wrong! The answer was 2")


        print("Game over")
        print(f"Final score: {self.score}")




