import random as rand
import turtle
word_list = [
# 406 total words
#3 letter words
    "act", "bat", "cat", "dog", "eel", "fun", "got", "hot", "ink", "jam",
    "key", "lap", "mop", "net", "oak", "paw", "qua", "rug", "sip", "tan",
    "urn", "van", "wax", "yes", "zoo", "aim", "bed", "cod", "dig", "end",
    "fig", "gem", "hex", "ivy", "jet", "kid", "lid", "mob", "nap", "odd",
    "peg", "qup", "rod", "sin", "tip", "use", "vet", "wet", "axe", "yak",
    "zag", "bib", "cup", "dim", "egg", "fog", "gym", "hug", "ill", "jot",
    "kin", "lip", "map", "nod", "oat", "pen", "qat", "row", "sly", "tug",
    "urn", "vow", "web", "yip", "zit", "ant", "box", "car", "dot", "elm",
    "fee", "gig", "hob", "ink", "jog", "kin", "leg", "mud", "nun", "oar",
    "peg", "quo", "run", "sip", "tar", "urn", "van", "wig", "yep", "zip",

    # 4 letter words
    "abcd", "able", "acid", "aged", "ajar", "ally", "amen", "ante", "aqua", "axis",
    "bark", "bats", "bend", "bide", "bind", "bony", "bore", "brag", "buff", "bull",
    "cane", "chic", "clam", "clip", "cope", "cute", "damp", "darn", "dart", "dash",
    "deck", "dive", "dock", "dust", "each", "echo", "edge", "envy", "exit", "eyed",
    "fade", "fame", "fend", "film", "flip", "fool", "frog", "fuel", "gale", "gear",
    "gild", "glow", "grab", "grim", "halt", "hazy", "heap", "heed", "hope", "huge",
    "icky", "idle", "inch", "item", "jazz", "jest", "jump", "jolt", "just", "keen",
    "keep", "knee", "knit", "lace", "lamp", "lend", "like", "link", "loop", "luck",
    "maid", "maze", "mild", "mind", "mole", "muse", "name", "nail", "neat", "node",
    "oath", "omen", "opal", "oval", "pace", "pale", "peak", "pint", "plot", "puma",
    "quad", "quiz", "quit", "race", "ramp", "reed", "rung", "rust", "sage", "seal",
    "skip", "slip", "snap", "soar", "span", "spin", "stab", "surf", "tame", "task",
    "tide", "tile", "toad", "trim", "tube", "tune", "twig", "ugly", "undo", "vase",
    "vent", "vote", "wane", "wean", "wink", "wisp", "wrap", "yarn", "year", "zone",

    # 5 letter words
    "apple", "beach", "blend", "crane", "dream", "ember", "flame", "grape", "happy", "jolly",
    "knife", "lemon", "magic", "noble", "ocean", "peace", "quilt", "rover", "sunny", "tramp",
    "unity", "vivid", "waste", "xerox", "yield", "zebra", "alive", "bison", "chime", "deity",
    "erase", "frost", "globe", "hatch", "index", "joust", "knead", "lunar", "mirth", "nymph",
    "olive", "plaza", "quash", "rider", "savor", "tally", "unzip", "vowel", "whale", "xenon",
    "youth", "zesty", "blink", "clasp", "douse", "elate", "flint", "glint", "hoist", "irate",
    "joker", "kiosk", "latch", "mango", "novel", "plush", "query", "rebel", "scamp", "truce",
    "ultra", "viper", "whisk", "xerox", "yarns", "zebra", "aloof", "braid", "crisp", "deter",
    "elite", "fable", "glide", "hound", "inert", "jumbo", "knack", "lotus", "merry", "nudge",
    "opera", "plump", "quake", "rival", "sleet", "thump", "urged", "vocal", "wrist", "xanax",
    "yacht", "zoned",

    # 6 letter words
    "banana", "camera", "dancer", "eleven", "floral", "guitar", "humble", "impact", "jigsaw", "knight",
    "laptop", "magnet", "noodle", "orange", "plague", "quasar", "rocket", "safari", "temper", "unique",
    "vector", "walnut", "xyloph", "yellow", "zigzag", "abound", "binary", "chance", "deluxe", "effort",
    "frozen", "grains", "hazard", "invent", "jungle", "kettle", "lizard", "minnow", "nuclei", "octave",
    "placid", "quiver", "rabbit", "sentry", "triple", "upload", "viewer", "whimsy", "xerox", "yogurt",
    "zenith", "abound", "breeze", "cascade", "decent", "effort", "fiddle", "grains", "humble", "impact",
    "jacket", "kettle", "lagoon", "mellow" ]


easy = ["T", "N", "S", "H", "H", "R", "D", "L", "U", "M"]
easy2 = ["A", "E", "I", "O", "U"]
hard = ["F", "W", "Y", "G", "P","B","V"]
hard2 = ["Z","Q","X","J","K"]


def get_difficulty(randword, difficulty):
    score = 0
    score += (len(randword) * 10)

    for letter in randword:
        if letter.upper() in easy:
            score -= 1
        if letter.upper() in easy2:
            score -= 2
        if letter.upper() in hard:
            score += 1
        if letter.upper() in hard2:
            score += 2

    
    if len(randword) == 3:
        if difficulty == 1:
            if score < 31:
                return True
        elif difficulty == 2:
            if score == 31:
                return True
        elif difficulty == 3:
            if score > 31:
                return True
        else:
            return False
    if len(randword) == 4:
        if difficulty == 1:
            if score < 40:
                return True
        elif difficulty == 2:
            if score == 40:
                return True
        elif difficulty == 3:
            if score > 40:
                return True
        else:
            return False
    if len(randword) == 5:
        if difficulty == 1:
            if score < 50:
                return True
        elif difficulty == 2:
            if score == 50:
                return True
        elif difficulty == 3:
            if score > 50:
                return True
        else:
            return False
    if len(randword) == 6:
        if difficulty == 1:
            if score < 60:
                return True
        elif difficulty == 2:
            if score == 60:
                return True
        elif difficulty == 3:
            if score > 60:
                return True
        else:
            return False
def diff_choice():
    difficulty = int(input("""Choose a difficulty
                 Enter 1 for Easy
                 Enter 2 for Medium
                 Enter 3 for Hard
                 Enter 4 to choose you own word"""))
    if difficulty == 4:
        while True:
            randword = input("Please enter your word: ")
            if randword.isalpha() and randword:
                for i in range(20):
                    print("_")
                break
            else:
                print("Invalid input. Please enter a valid string.")
    else:
        randword = rand.choice(word_list)
        while True:
            randword = rand.choice(word_list)
            if not get_difficulty(randword, difficulty):
                continue  # Pick a new word if difficulty criteria not met
            else:
                break
    return randword





def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def draw_hangman(strikes):
    t = turtle.Turtle()
    t.speed(2)

    if strikes == 1:
        t.penup()
        t.goto(-50, 0)
        t.pendown()
        t.circle(30)  # Head
    elif strikes == 2:
        t.penup()
        t.goto(-50, 0)
        t.pendown()
        t.right(90)
        t.forward(80)  # Body
    elif strikes == 3:
        t.penup()
        t.goto(-50, -40)
        t.pendown()
        t.left(45)
        t.forward(40)  # Left arm
    elif strikes == 4:
        t.penup()
        t.goto(-50, -40)
        t.pendown()
        t.right(225)
        t.forward(40)  # Right arm
    elif strikes == 5:
        t.penup()
        t.goto(-50, -80)
        t.pendown()
        t.left(225)
        t.forward(40)  # Left leg
    elif strikes == 6:
        t.penup()
        t.goto(-50, -80)
        t.pendown()
        t.right(45)
        t.forward(40)  # Right leg
    


def hangman(word):
    strikes = 0
    guessed_letters = []

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while '_' in display_word(word, guessed_letters):
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                strikes += 1
                draw_hangman(strikes)
                print(f"Strikes: {strikes}")
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word, guessed_letters))

        if strikes == 6:
            print("Sorry, you're out of strikes. The word was:", word)
            break

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word:", word)

def main():
    chosen_word = diff_choice()
    hangman(chosen_word)

main()
