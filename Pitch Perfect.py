import winsound
import random
while True:
    frequency = random.randint(27,4186)
    duration = 2000 
    winsound.Beep(frequency, duration)

    guess = input()

    while guess == "r":
        winsound.Beep(frequency, duration)
        guess = input()
    
    print(frequency)
    
    next = input()
    while next != "":
        if next == "r":
            winsound.Beep(frequency, duration)
        next = input()
        
