"""
Complete the script.
"""
#This is a practice script per Task 4 of Module 1 which shows exmples of /n
# input(), print(), type(), int(), float(), min(), max(),assigning variables, /n
# and communication with the user (using useful print()) and in code (such as this comment).


print('Hello Python World!')
print()
print('This is my first time writing code!')
print("I've learned more in past week, than I have in the past year, and I'm LOVING the challenge!")
print("The domain I chose for this class is 'Baseball.'/n
I will be using that topic to show off what I've learned so far")
print()
print("Well, enough about me; let's talk about you")
name = input("What is your name?: ")
print("Hello " + name.capitalize() + "!")
print()

games_per_team =  162
teams_per_division =  15
number_of_divisions =  2


response = input("Would you like to see how I can assign variables? (y/n)")

if response == "y":
    print()
    print("Great! I'm going to use f'strings to show you the variables I've assigned in my code.")
    print()
    print("Let's see how many baseball games we can theoretically watch per year...")
    print(f"The total number of games each MLB team plays per season is={games_per_team}.")
    print(f"There are={teams_per division} teams per division.")
    print(f"The MLB has={number_of_divisions} divisions, which are the National and the American Leagues")
    print(f"That means the number of games I get to watch each season is={games_per_team}*{teams_per_division}*{number_of_divisions}!"
    print()
    print("That's a lot of baseball to watch!")
    print()

if response == "n":
    print()
    print("Are you sure? I worked so hard on this code! (y/n)")
    response = input("That's ok can I still have an A for this assignment?")
        if resonse == "y"
            print()
            print(Thank you, you're the best Dr. Case!')
        if resonse == "n"
            print()
            print('That's ok, I'm still learning a lot.')

input()
print()
int()
float()
min()
max()
