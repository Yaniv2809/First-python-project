import math_game
import password_game
import memory_game

def main():
    while True:
        print("\n==========================")
        print("   W O R L D  O F  G A M E S   ")
        print("==========================")
        print("1. Math Quiz")
        print("2. Password Guess")
        print("3. Memory Game")
        print("4. Exit")

        choice = input("Select a game (1-4): ")

        if choice == '1':
            player_name = input("Enter player name for Math Game: ")
            game = math_game.MathGame(player_name)
            game.play()

        elif choice == '2':
            game = password_game.PasswordGame(3)
            game.play()

        elif choice == '3':
            game = memory_game.MemoryGame()
            game.play()

        elif choice == '4':
            print("Goodbye! Thanks for playing.")
            break

        else:
            print("Invalid selection. Please try again.")

main()