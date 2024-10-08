import musicpy as mp
import string
import random
import librosa

BPM = 50

# notes = ['A0', 'A#0', 'B0', 
#  'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1',
#  'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
#  'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
#  'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
#  'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
#  'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6',
#  'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7',
#  'C8']

notes = ['B0','B1','B2','B3','B4','B5','B6','B7']

def piano(user):
    # get random note
    noteStr = random.choice(notes)

    noteMp = mp.note(noteStr[:-1], int(noteStr[-1]))

    # play note
    play = lambda: mp.play(noteMp, wait=True, bpm=BPM)

    # play C4
    # mp.play(mp.note('C', 4), wait=True, bpm=BPM)
    
    play()

    guess = input()

    # get user's guess
    while guess == "r":
        play()
        guess = input()

    # display answer
    print(noteStr, round(librosa.note_to_hz(noteStr), 1))

    next = input()
    while next != "":
        if next == "r":
            play()
        if "play " in next:
            mp.play(mp.note(next[-2:])) 
        if next == "q":
            return False
        next = input()
    return True