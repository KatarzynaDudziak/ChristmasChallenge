import time
import sys
import winsound


def play_jingle_bells(letters_notes, tones, dict_of_frequency):
    for (letter, tone) in zip(letters_notes, tones):
        if letter in dict_of_frequency.keys():
            frequency = dict_of_frequency[letter]
            duration = tone * 200
            sys.stdout.write('*')
            sys.stdout.flush()
            winsound.Beep(frequency, duration)


def main():
    tones = [2, 2, 4, 2, 2, 4, 2, 2, 2, 1, 8, 2, 2, 2, 1, 2, 2, 2, 1, 1,
            2, 2, 2, 2, 4, 4, 2, 2, 4, 2, 2, 4, 2, 2, 2, 1, 8, 2, 2, 2,
            1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 8, 2, 2, 2, 2, 4, 1, 1, 2, 2,
            2, 2, 8, 2, 2, 2, 2, 8, 2, 2, 2, 2, 8, 2, 2, 2, 2, 8, 2, 2,
            2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]

    letters_notes = ['E','E','E','E','E','E','E','G','C','D','E','F','F','F','F','F','E','E',
                    'E','E','E','D','D','E','D','G','E','E','E','E','E','E','E','G','C','D',
                    'E','F','F','F','F','F','E','E','E','E','G','G','F','D','C','D','B','A',
                    'G','D','D','D','D','B','A','G','E','E','c','B','A','F','D','D','c','A',
                    'B','D','B','A','G','D','D','B','A','G','E','E','E','c','B','A','D','D',
                    'D','D','E','D','c','A','G',]

    dict_of_frequency = {
            'c' : 262,
            'C' : 261,
            'D' : 293,
            'E' : 329,
            'F' : 349,
            'G' : 392,
            'A' : 440
    }

    play_jingle_bells(letters_notes, tones, dict_of_frequency)

if __name__=='__main__':
    main()
