#python puzzle Text base Game
#FIND YOUR HOME

import cmd
import textwrap
import sys
import os
import time
from random import *

scrren_width = 100



##player setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'a1'
        self.won = False
        self.solves = 0
        self.feeling = ''

myPlayer = player()




### Intro screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option = input("< ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('#' * 45)
    print("               FIND YOUR HOME                ")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    print('     - Copyright 2019 aliershadian.com -     ')
    title_screen_selections()
    

def help_menu():
    os.system('clear')
    print("")
    print('#' * 45)
    print("               FIND YOUR HOME                ")
    print('#' * 45)
    print('#' * 45)
    print("      -Programmed By Ali Ershadian-      ")
    print("~" * 45)
    print("Type a command such as 'move' then 'left'")
    print("to nagivate the map of the puzzle.\n")
    print("Type a command 'where'")
    print("to see where you are.\n")
    print("Inputs such as 'look' or 'examine' will")
    print("let you interact with puzzles in rooms.\n")
    print("Puzzles will require various input and ")
    print("possibly answers from outside knowledge.\n")
    print("Please ensure to type in lowercase for ease.\n")
    print('#' * 45)
    print("\n")
    print('#' * 45)
    print("    Please select an option to continue.     ")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    print('     - Copyright 2019 aliershadian.com -     ')
    title_screen_selections()



### MAP  ###
ZONENAME = ''
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'downd', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

places = ["a1","a2","a3","a4","b1","b2","b3","b4","c1","c2","c3","c4","d1","d2","d3","d4"]
solved_places = {'a1' : False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}
        
zonemap = {
    'a1' : {
        ZONENAME : 'Westton',
        EXAMINATION : 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?',
        SOLVED : 'echo',
        UP : '', 
        DOWN : 'b1', 
        LEFT : '', 
        RIGHT : 'a2',
        },
    'a2' : {
        ZONENAME : 'Byport',
        EXAMINATION : 'You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy.',
        SOLVED : 'candle',
        UP : '', 
        DOWN : 'b2', 
        LEFT : 'a1', 
        RIGHT : 'a3',
        },
    'a3' : {
        ZONENAME : 'Merrowmeadow',
        EXAMINATION : 'I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? ',
        SOLVED : 'map',
        UP : '', 
        DOWN : 'b3', 
        LEFT : 'a2', 
        RIGHT : 'a4',
        },
    'a4' : {
        ZONENAME : 'Faybarrow',
        EXAMINATION : 'What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?',
        SOLVED : 'r',
        UP : '', 
        DOWN : 'b4', 
        LEFT : 'a3', 
        RIGHT : '',
        },
    'b1' : {
        ZONENAME : 'Esterflower',
        EXAMINATION : 'What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word? ',
        SOLVED : 'heroine',
        UP : 'a1', 
        DOWN : 'c1', 
        LEFT : '', 
        RIGHT : 'b2',
        },
    'b2' : {
        ZONENAME : 'Esterbell',
        EXAMINATION : 'What English word has three consecutive double letters? ',
        SOLVED : 'bookkeeper',
        UP : 'a2', 
        DOWN : 'c2', 
        LEFT : 'b1', 
        RIGHT : 'b3',
        },
    'b3' : {
        ZONENAME : 'Deepkeep',
        EXAMINATION : 'I come from a mine and get surrounded by wood always. Everyone uses me. What am I? ',
        SOLVED : 'pencil lead',
        UP : 'a3', 
        DOWN : 'c3', 
        LEFT : 'b2', 
        RIGHT : 'b4',
        },
    'b4' : {
        ZONENAME : 'SidersVillage',
        EXAMINATION : 'What disappears as soon as you say its name? ',
        SOLVED : 'silence',
        UP : 'a4', 
        DOWN : 'c4', 
        LEFT : 'b3', 
        RIGHT : '',
        },
    'c1' : {
        ZONENAME : 'Corcastle',
        EXAMINATION : 'I have keys, but no locks and space, and no rooms. You can enter, but you can’t go outside. What am I?',
        SOLVED : 'keyboard',
        UP : 'b1', 
        DOWN : 'd1', 
        LEFT : '', 
        RIGHT : 'c2',
        },
    'c2' : {
        ZONENAME : 'Coldpine',
        EXAMINATION : 'What gets wet while drying?',
        SOLVED : 'towel',
        UP : 'b2', 
        DOWN : 'd2', 
        LEFT : 'c1', 
        RIGHT : 'c3',
        },
    'c3' : {
        ZONENAME : 'Highbeach',
        EXAMINATION : 'First, think of the color of the clouds. Next, think of the color of snow. Now, think of the color of a bright full moon. Now answer quickly what do cows drink?',
        SOLVED : 'water',
        UP : 'b3', 
        DOWN : 'd3', 
        LEFT : 'c2', 
        RIGHT : 'c4',
        },
    'c4' : {
        ZONENAME : 'Shadowsage',
        EXAMINATION : 'First you eat me, then you get eaten. What am I?',
        SOLVED : 'fishhook',
        UP : 'b4', 
        DOWN : 'd4', 
        LEFT : 'c3', 
        RIGHT : '',
        },
    'd1' : {
        ZONENAME : 'Windbush',
        EXAMINATION : 'What comes once in a minute, twice in a moment, but never in a thousand years?',
        SOLVED : 'm',
        UP : 'c1', 
        DOWN : '', 
        LEFT : '', 
        RIGHT : 'd2',
        },
    'd2' : {
        ZONENAME : 'Bymist',
        EXAMINATION : 'Which word in the dictionary is always spelled incorrectly?',
        SOLVED : 'incorrectly',
        UP : 'c2', 
        DOWN : '', 
        LEFT : 'd1', 
        RIGHT : 'd3',
        },
    'd3' : {
        ZONENAME : 'Coldtown',
        EXAMINATION : 'What breaks on the water but never on land?',
        SOLVED : 'wave',
        UP : 'c3', 
        DOWN : '', 
        LEFT : 'd2', 
        RIGHT : 'd4',
        },
    'd4' : {
        ZONENAME : 'Freyfield',
        EXAMINATION : 'What can be measured but not seen?',
        SOLVED : 'time',
        UP : 'c4', 
        DOWN : '', 
        LEFT : 'd3', 
        RIGHT : '',
        }, 
    }



### GAME INTERACTIVITY ###
def print_location():
    printInGame('\n' + ('#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))) + "\n", 0.05)
    printInGame('# ' + zonemap[myPlayer.location][ZONENAME] + ' #', 0.05)
    #print('# '+ myPlayer.location.upper() + ' #')
    printInGame('\n' + ('#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))), 0.05)

def prompt():
    printInGame("\n" + "===========================\n", 0.05)
    printInGame("What would yo like to do?", 0.05)
    action = input("> ")
    acceptable_actions= ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'where']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine()
    elif action.lower() == 'where':
        print_location()

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up' , 'north']:
        if zonemap[myPlayer.location][UP] == '':
            printInGame("\n~~~~~~~\nThere is no space in north.\n", 0.05)
        else:
            destination = zonemap[myPlayer.location][UP]
            movement_handler(destination)
    elif dest in ['left' , 'west']:
        if zonemap[myPlayer.location][LEFT] == '':
            printInGame("\n~~~~~~~\nThere is no space in west.\n", 0.05)
        else:
            destination = zonemap[myPlayer.location][LEFT]
            movement_handler(destination)
    elif dest in ['right' , 'east']:
        if zonemap[myPlayer.location][RIGHT] == '':
            printInGame("\n~~~~~~~\nThere is no space in east.\n", 0.05)
        else:
            destination = zonemap[myPlayer.location][RIGHT]
            movement_handler(destination)
    elif dest in ['down' , 'south']:
        if zonemap[myPlayer.location][DOWN] == '':
            printInGame("\n~~~~~~~\nThere is no space in south.\n", 0.05)
        else:
            destination = zonemap[myPlayer.location][DOWN]
            movement_handler(destination)

def movement_handler(destination):
    #printInGame("\n" + "You have moved to the " + destination + ".", 0.05)
    myPlayer.location = destination
    print_location()

def player_examine():
    if solved_places[myPlayer.location]  == False:
        printInGame("we have a puzzle for you!!\n", 0.01)
        printInGame(zonemap[myPlayer.location][EXAMINATION]+"\n", 0.01)
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    else:
        printInGame("You have already exhausted this zone.\n", 0.01)

def checkpuzzle(puzzle_answer):
    if puzzle_answer == (zonemap[myPlayer.location][SOLVED]):
        solved_places[myPlayer.location] = True
        myPlayer.solves += 1
        printInGame("You have solved the puzzle. Onwards!", 0.01)
        printInGame("\nPuzzles solved: " + str(myPlayer.solves) , 0.01)
        if myPlayer.location == 'b4':
            printInGame("\nThis is your home and you solved the puzzle!\nWelcome to your sweet home!\nCONGRATS!\nYOU HAVE WON!", 0.05)
            myPlayer.won = True
            time.sleep(0.4)
            sys.exit()

        if myPlayer.solves == 3:
            printInGame("\n****************************", 0.05)
            printInGame("\nWe have found your home, It's in "+ zonemap['b4'][ZONENAME], 0.05)
            printInGame("\n****************************", 0.05)
            

        
    else:
	    printInGame("Wrong answer! Try again.\n~~~~~~~~~~~~~", 0.01)
        




### GAME FUNCTIONALITY ###
def main_game_loop():
    while myPlayer.won is False:
        prompt()
        
def printInGame(text, speed):
    for char in text : 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
        
def setup_game():
    x = randint(0, 15)
    myPlayer.location = places[x]
    os.system('clear')

    question1 = "Hello there, what's your name?\n"
    printInGame(question1, 0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    answer1= "It's awesome to know you " + player_name.upper() + "\n"
    printInGame(answer1, 0.05)



    question2 = "My dear friend " + player_name.upper() + ", how are you feeling?\n"
    printInGame(question2, 0.05)
    feeling = input("> ")
    myPlayer.feeling = feeling.lower()

    good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving']
    hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult']
    bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']

    if myPlayer.feeling in good_adj:
        feeling_string = "I am glad you feel"
    elif myPlayer.feeling in hmm_adj:
	    feeling_string = "that is interesting you feel"
    elif myPlayer.feeling in bad_adj:
	    feeling_string = "I am sorry to hear you feel"
    else:
	    feeling_string = "I do not know what it is like to feel"

    answer2 = "Well then, " + player_name.upper() + ", " + feeling_string + " " + myPlayer.feeling + ".\n"
    printInGame(answer2, 0.05)

        
    question3 = "what astrological you wnat to be?\n"
    question3added = "You can play as a:\n"
   
    printInGame(question3, 0.05)
    printInGame(question3added, 0.01)

    printInGame("# ♈ Aries (The Ram)\n" , 0.01)
    printInGame("# ♉ Taurus (The Bull)\n", 0.01)
    printInGame("# ♊ Gemini (The Twins)\n", 0.01)
    printInGame("# ♋ Cancer (The Crab)\n", 0.01)
    printInGame("# ♌ Leo (The Lion)\n", 0.01)
    printInGame("# ♍ Virgo (The Virgin)\n", 0.01)
    printInGame("# ♎ Libra (The Scales)\n", 0.01)
    printInGame("# ♏ Scorpio (The Scorpion)\n", 0.01)
    printInGame("# ♐ Sagittarius (Centaur)\n", 0.01)
    printInGame("# ♑ Capricorn (The Goat)\n", 0.01)
    printInGame("# ♒ Aquarius (The Water Bearer)\n", 0.01)
    printInGame("# ♓ Pisces (The Fish)\n", 0.01)
    
    player_job = input("> ")
    valid_jobs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a "+ player_job + "!")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a "+ player_job + "!")

    if myPlayer.job is 'aries':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'taurus':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'gemini':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'cancer':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'leo':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'virgo':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'libra':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'scorpio':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'sagittarius':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'capricorn':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'aquarius':
        self.hp = 60
        self.mp = 60
    elif myPlayer.job is 'pisces':
        self.hp = 60
        self.mp = 60

    valid_jobs = {'aries' : "Strengths: courageous- determined- confident- enthusiastic- optimistic- honest- passionate \nWeaknesses: impatient- moody- short-tempered- impulsive- aggressive",
                  'taurus' : "Strengths: reliable- patient- practical- devoted- responsible- stable \nWeaknesses: stubborn- possessive- uncompromising",
                  'gemini' : "Strengths: gentle- affectionate- curious- adaptable- ability to learn quickly and exchange ideas \nWeaknesses: nervous- inconsistent- indecisive",
                  'cancer' : "Strengths: tenacious- highly imaginative- loyal- emotional- sympathetic- persuasive \nWeaknesses: moody- pessimistic- suspicious- manipulative- insecure",
                  'leo' : "Strengths: creative- passionate- generous- warm-hearted- cheerful- humorous \nWeaknesses: arrogant- stubborn- self-centered- lazy- inflexible",
                  'virgo' : "Strengths: loyal- analytical- kind- hardworking- practical \nWeaknesses: shyness- worry- overly critical of self and others- all work and no play",
                  'libra' : "Strengths: cooperative- diplomatic- gracious- fair-minded- social \nWeaknesses: indecisive- avoids confrontations- will carry a grudge- self-pity",
                  'scorpio' : "Strengths: resourceful- brave- passionate- stubborn- a true friend \nWeaknesses: distrusting- jealous- secretive- violent",
                  'sagittarius' : "Strengths: generous- idealistic- great sense of humor \nWeaknesses: promises more than can deliver- very impatient- will say anything no matter how undiplomatic",
                  'capricorn' : "Strengths: responsible- disciplined- self-control- good managers \nWeaknesses: know-it-all- unforgiving- condescending- expecting the worst",
                  'aquarius' : "Strengths: Progressive- original- independent- humanitarian \nWeaknesses: Runs from emotional expression- temperamental- uncompromising- aloof",
                  'pisces' : "Strengths: Compassionate- artistic- intuitive- gentle- wise- musical \nWeaknesses: Fearful- overly trusting- sad- desire to escape reality- can be a victim or a martyr"}

    printInGame(valid_jobs[myPlayer.job] + "\n", 0.1)
    printInGame("Now, you know all strengths and weaknesses of your character.\n\n", 0.1)

    printInGame("But, "+ player_name.upper() +", don't take it too serious, it's a game jam not a AAA Game, we don't yet use this astrological signs in our game :):):)", 0.1)
    os.system('clear')
    
    #Introduction
    question4 = "Welcome "+player_name+ " the "+player_job+".\n"
    printInGame(question4, 0.05)

    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I Hope it greets you well!\n"
    speech3 = "Just make sure you don't get too lost...\n"
    speech4 = "Hehehehe...\n"

    printInGame(speech1, 0.03)
    printInGame(speech2, 0.03)
    printInGame(speech3, 0.1)
    printInGame(speech4, 0.2)

    os.system('clear')
    print("###################################")
    print("#         Let's Start Now!        #")
    print("###################################")
    main_game_loop()



title_screen()

