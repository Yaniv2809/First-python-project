import random
import time

class MemoryGame:
    def __init__(self):
        self.sequence = []
        self.sequence_length = 5

    def play(self):
        print("\n--- Memory Game ---")
        
        print(f"Memorize the sequence of {self.sequence_length} numbers!")
        time.sleep(1)


        self.sequence = []
        count = 0
        while count < self.sequence_length:
            num = random.randint(1, 20)
            self.sequence.append(num)
            count = count + 1  # קידום המונה

       
        print("Sequence: ", self.sequence)
        time.sleep(2)


        print("\n" * 100)
        print("Time's up! Recall the numbers.")

        while True:
            user_input = input("Enter numbers separated by space (or 'q' to quit): ")

            if user_input == 'q':
                print("Gave up? The sequence was:", self.sequence)
                break

            try:

                input_list_strings = user_input.split()
                user_sequence = []

                i = 0

                while i < len(input_list_strings):
                   
                    current_string = input_list_strings[i]
                    number = int(current_string)
                    user_sequence.append(number)
                    i = i + 1

               
                if user_sequence == self.sequence:
                    print("AMAZING! You have a perfect memory!")
                    break
                else:
                   
                    correct_count = 0
                    j = 0  # מונה חדש לבדיקה

                    #  לרוץ כל עוד לא הגענו לסוף של אחת הרשימות
                    while j < len(self.sequence) and j < len(user_sequence):
                        if self.sequence[j] == user_sequence[j]:
                            correct_count = correct_count + 1
                        j = j + 1

                    print("Not quite. You got " + str(correct_count) + " correct numbers in place. Try again!")

            except ValueError:
                print("Please enter valid numbers only.")





