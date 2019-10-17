import random
import time
print("\t \t Sveiciens tev Hangman.")
vards = input("Ka tevi sauc? :")
print("Lai tev izdodas",vards,".")
time.sleep(4)

def get_guess():
  drawings = (
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
    |   ||   
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
    |   |||
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
    |   |||
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
    |   |||
    |    |
    |   | 
    |   |
    |    
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   |||
    |    |
    |   | |
    |   | |
    |   
    |  
    ----------
    """)
  # Set the dashes to the length of the secret word and set the amount of guesses 
  # the user has to 10
  dashes = "-" * len(secret_word)
  guesses_left = 0
  lvl = 1
  

  
  # This will loop as long as BOTH conditions are true:
  # 1. The number of guesses of left is greater than -1
  # 2. The dash string does NOT equal the secret word
  while guesses_left < 8 and not dashes == secret_word:
    
    # Print the amount of dashes and guesses left
    print(drawings[guesses_left])
    print(dashes)
    print ("nepareizi minejumi",str(guesses_left))
    print("limenis",str(lvl))
    # Ask the user for input
    guess = input("Guess:")
    
    # Conditions that will print out a message according to
    # invalid inputs
    if len(guess) != 1:
      print ("Tev ir jaatbild tikai ar vienu vardu.")
      
    # If the guess is in the secret word then we updtae dashes to replace the
    # corresponding dash with the correct index the guess belongs to in the 
    # secret word
    elif guess in secret_word:
      print ("Sis burts ir pasleptaja varda.")
      dashes = update_dashes(secret_word, dashes, guess)
      
    # If the guess is wrong then we display a message and subtract
    # the amount of guesses the user has by 1
    else:
      print ("Burts nav pasleptaja varda.")
      guesses_left = guesses_left+1
    
  if guesses_left == 8:
    print ("Tu zaudeji, vards bija: " + str(secret_word))
    input("""Vai velies turpinat speli?
                Ja(Y)      Ne(N)
                                :""").lower
    if input == "y":
      get_guess();

    elif input == "n":
      time.sleep(10)
      exit
    
      
  # If the dash string equals the secret word in the end then the
  # user wins
  else:
    print ("Malacis! Vards bija: " + str(secret_word))
   

# This function updates the string of dashes by replacing the dashes
# with words that match up with the hidden word if the user manages to guess
# it correctly
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
  return result
 
    
words = ["aka", "lava", "suns", "lampa", "sigulda", "banka", "dators", "loks", "upe", "koks", "virve"]
secret_word = random.choice(words)
get_guess()