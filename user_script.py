"""
Complete the script.
"""
# This is a practice script per Task 4 of Module 1 which shows exmples of /n
# input(), print(), type(), int(), float(), min(), max(),assigning variables, /n
# and communication with the user (using useful print()) and in code (such as this comment).

import statistics
print()
print()
print('Hello Python World!')
print()
print('This is my first time writing code!')
print()
print("I've learned more in past week, than I have in the past year; and I'm LOVING the challenge!")
print()
print("The domain I chose for this class is 'Baseball'")
print()
print("I will be using that topic to show off what I've learned so far.")
print()
print("Well, enough about me; let's talk about you")
name = input("What is your name?: ")
print()
print()
print("Hello " + name.capitalize() + "! Thank you for reading my code!")
print("=============================================================")
print()
print("Let me show you some of the functions I've learned from the Python Standard Library")


# Here are the batting averages of the players on the St. Louis Cardinals roster
stl_avg = [.317,
           .293,
           .281,
           .270,
           .267,
           .265,
           .256,
           .253,
           .236,
           .228,
           .228,
           .226,
           .215,
           .214,
           .189,
           .188,
           .176,
           .157,
           .154,
           .150,
           .111,
           .000,
           ]

mean = statistics.mean(stl_avg)
median = statistics.median(stl_avg)
mode = statistics.mode(stl_avg)
var = statistics.variance(stl_avg)
stdev = statistics.stdev(stl_avg)
lowest = min(stl_avg)
highest = max(stl_avg)

# using variable colon formatting to avoid unnecessary digits (e.g. .3f).
print()
print()
print(f"Here's some St. Louis Cardinals 2022 batting average data: {stl_avg}")
print()
print("Here's how the Redbirds batted last year:")
print(f"   mean={mean:.3f}")
print(f"   median={median:.3f}")
print(f"   mode={mode:.3f}")
print(f"   lowest={lowest: .3f}")
print(f"   highest={highest: .3f}")
print(f"   range=({lowest: .3f} - {highest: .3f})")
print()
print("Descriptive statistics include measures of spread:")
print(f"   var={var:.3f}")
print(f"   stddev={stdev:.3f}")
print("The %RSD is another helpful statistic to assess variability")
print(f"   %RSD={round(stdev/mean*100)}%")
print()
print()
print()

games_per_team = int(162)
teams_per_division = int(15)
number_of_divisions = int(2)
total_games = int(games_per_team * teams_per_division * number_of_divisions / 2)
total_mlb_teams = teams_per_division + teams_per_division

response = input("Would you like to see how I can assign variables? (y/n)")

if response == "y":
    print()
    print("Great! I'm going to use f'strings to show you the variables I've assigned in my code.")
    print()
    print("Let's see how many baseball games we can theoretically watch per year...")
    print(
        f"The total number of games each MLB team plays per season is {games_per_team}.")
    print(f"There are {teams_per_division} teams per division.")
    print(f"Thus there are {total_mlb_teams} teams in the MLB.")
    print(
        f"The MLB has {number_of_divisions} divisions, which are the National and the American Leagues.")
    print(
        f"That means the number of games I get to watch each season is {total_games}! Note that you have to divide by 2, since there are 2 teams that play in each game.")
    print()
    print("That's a lot of baseball to watch!")
    print()
if response == "n":
    print()
    response = input("Are you sure? I worked so hard on this code! (y/n)")
    if response == "y":
        response = (
            input("That's ok, can I still have an A for this assignment? (y/n)"))

        if response == "y":
            print()
            print("Thank you, you're the best Dr. Case!")
        if response == "n":
            print()
            print("That's ok, I'm still learning a lot and having tons of fun.")
            print()
    if response == "n":
        print()
        print("Great! I'm glad you changed your mind. I'm going to use f'strings to show you the variables I've assigned in my code.")
        print()
        print("Let's see how many baseball games we can theoretically watch per year...")
        print(
            f"The total number of games each MLB team plays per season is={games_per_team}.")
        print(f"There are={teams_per_division} teams per division.")
        print(f"Thus there are {total_mlb_teams} teams in the MLB.")

        print(
            f"The MLB has={number_of_divisions} divisions, which are the National and the American Leagues")
        print(
            f"That means the number of games I get to watch each season is {total_games}! Note that you have to divide by 2, since there are 2 teams that play in each game.")
        print("That's a lot of baseball to watch!")
        print()

print()
print()
print("That was fun! Have a great day.")
print()
print()
