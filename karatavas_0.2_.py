import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |    |
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /|   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /|\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /|\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /|\
 |    |
 |   | 
 |    
 |    
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /|\
 |    |
 |   | |
 |   
 |   
 |  
----------
""")

vardubanka = ("galds", "aka", "suns", "jaka", "lauva", "sigulda", "latvija")
word = random.choice(vardubanka)
POSITIVE_SAYINGS = ("Labs darbs!", "Lieliski!")
MAX_WRONG = len(word) - 1
so_far = (' _ ') * len(word)
used = []
wrong = 0

print("\t \t Sveiciens tev Hangman.")
print()
input("Lai saktu, nospied ENTER: ")

while wrong < MAX_WRONG and so_far != word:
    print()
    print(HANGMAN[wrong])
    print("Vards: ", so_far)
    print("Izmantotie burti: ", used)

    guess = input("Mini burtu: ")
    sleep(1) # Time delay - allows userfriendly reading
    print()

    while guess in used:
        print("Megini velreiz, tu jau esi izmantojis so burtu.")
        guess = input("Mini burtu: ")
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS),"...Atjauninu vardu...")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new 

    else:
        print("Neparezi! Megini velreiz!")
        wrong += 1

print("Calculating result...")
sleep(1)
if wrong == MAX_WRONG:
    spele = raw_input("Ja gibi spelet velreiz, nospied (y) ja ne (n)")
    if spele == "y":
        HANGMAN
        
        
     

else:
    print("Uzvara! Apsveicu tevi!")

print()
print()
input("Ja velies beigt spelet, nospie ENTER: ")