import time
import os

with open('Rockin\'_around_the_Christmas_Tree.txt', 'r') as f:
    os.system('cls')
    for line in f:
        print(line)
        time.sleep(3)
        os.system('cls')