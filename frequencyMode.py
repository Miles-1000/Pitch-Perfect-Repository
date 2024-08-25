import time
import winsound
import random
import librosa

def log_guess(frequency, guess, file_name):
    with open(file_name, "a") as f:
        current_time_seconds = int(time.time())
        f.write(f"{frequency}\t{guess}\t{current_time_seconds}\n")

def frequency(user):
    frequency = random.randint(27,4186)
    duration = 2000 
    winsound.Beep(frequency, duration)

    guess = input()

    # get user's guess
    while guess == "r":
        winsound.Beep(frequency, duration)
        guess = input()
    
    # display answer
    print(frequency)

    # log user's guess
    log_guess(frequency, guess, user)
    
    # do not log after answer has been given
    next = input()
    while next != "":
        if next == "r":
            winsound.Beep(frequency, duration)
        elif next == "q":
            return False
        next = input()
    
    return True