import random

# Words for each difficulty level
easy_words = ['cat', 'dog', 'hat', 'red', 'top', 'pen', 'mat', 'cup', 'sun', 'box',
              'fan', 'zip', 'joy', 'key', 'oak', 'bus', 'bug', 'hen', 'jar', 'map']
medium_words = ['book', 'duck', 'jump', 'king', 'lion', 'nest', 'rain', 'star', 'tree', 'wave',
                'zebra', 'beef', 'club', 'dusk', 'echo', 'fury', 'goat', 'hero', 'jazz', 'kite']
hard_words = ['alcohol', 'biology', 'chicken', 'diamond', 'elephant', 'festival', 'giraffe', 'hospital', 'jungle', 'kangaroo',
              'language', 'mountain', 'network', 'oxygen', 'physics', 'quality', 'rainbow', 'surgery', 'trumpet', 'universe']

# Hangman images
hangman_images = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

# Function to get a random word from the list
def get_random_word(difficulty_level):
    if difficulty_level == 'easy':
        return random.choice(easy_words)
    elif difficulty_level == 'medium':
        return random.choice(medium_words)
    elif difficulty_level == 'hard':
        return random.choice(hard_words)

# Function to display the current state of the game
def display_game_state(word, guessed_letters, num_incorrect_guesses):
    # Print the hangman image
    print(hangman_images[num_incorrect_guesses])
    
    # Print the length of the word
    print("The word has", len(word), "letters.")
    
    # Print the word with the correctly guessed letters filled in
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

# Function to check if the game is over
def is_game_over(word, guessed_letters, num_incorrect_guesses):
    if num_incorrect_guesses >= 6:
        return True
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to play the game
def play_game():
    # Welcome message and difficulty level selection
    print('Welcome to Hangman!')
    difficulty_level = input('Please choose a difficulty level (easy, medium, or hard): ').lower()
    if difficulty_level not in ['easy', 'medium', 'hard']:
        print('Invalid difficulty level. Please try again.')
        play_game()
        return
    
    # Get a random word and initialize variables
    word = get_random_word(difficulty_level)
    guessed_letters = set()
    num_incorrect_guesses = 0
    
    # Game loop
    while not is_game_over(word, guessed_letters, num_incorrect_guesses):
        display_game_state(word, guessed_letters, num_incorrect_guesses)
        
        # Get user input for a letter
        letter = input('Guess a letter: ').lower()
        if len(letter) != 1 or not letter.isalpha():
            print('Invalid input. Please enter a single letter.')
            continue
        if letter in guessed_letters:
            print('You already guessed that letter. Try again.')
            continue
        
        # Check if the letter is in the word
        if letter in word:
            guessed_letters.add(letter)
            print('Correct!')
        else:
            num_incorrect_guesses += 1
            print('Incorrect.')
        
    # Print final game state
    display_game_state(word, guessed_letters, num_incorrect_guesses)
    
    # Print win/loss message
    if num_incorrect_guesses >= 6:
        print('You lose! The word was:', word)
    else:
        print('Congratulations, you win! The word was:', word)
    
    # Ask user if they want to play again
    play_again = input('Do you want to play again? (yes or no) ').lower()
    if play_again == 'yes':
        play_game()
    else:
        print('Thanks for playing!')
        
# Start the game
play_game()  
