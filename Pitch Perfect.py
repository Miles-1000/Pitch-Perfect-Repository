import pianoMode
import frequencyMode

user = ""
while user not in ["r", "b"]:
    user = input("Enter 'r' for ruben or 'b' for bastiaan: ")

if user == "r":
    user = "ruben.txt"
elif user == "b":
    user = "bastiaan.txt"

while True:
    mode = input("Piano(p) or Frequency(f): ")

    if mode == "p":
        while pianoMode.piano(user): ...
    elif mode == "f":
        while frequencyMode.frequency(user): ...
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
