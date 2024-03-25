# The Stanley Parable employee number 427's work in Python 2.7.5

import random
import time

# Time when you start
t = time.localtime(time.time())
localtime = time.asctime(t)
string = "Date and time: " + time.asctime(t)
print(string)

# Introduction
print(
    "This is the job of a man named Stanley. Stanley worked for a company in a big building where he was Employee #427. Employee #427's"
    "job was simple: he sat at his desk in Room 427 and he pushed buttons on a keyboard. Orders came to him through a monitor on his desk telling him what buttons to push and in what order.")

# main_code function
def main_code():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    random_output = random.choice(letters)
	
    print(">>> Enter the letter " + random_output)
    input_letter = raw_input(">>> ")
    if input_letter != random_output:
        print("You had one job! ")
    print("----------------------")
    

# Execute the function
for i in range(1000):
    main_code()
