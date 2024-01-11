# mastermind game playing using information thoery

import random
import math

''' 1. pick code and display it so we can see'''


def choose_code():
    Num_Total = [1,2,3,4,5,6]
    Code = ''
    i = 0
    while i in range(4):
        Code = Code + str(random.choice(Num_Total))
        i += 1
    print(Code)
    return Code


''' 2. Get clue based on the guess and the actual code'''

def Clues(code,guess):
    circle = ''
    check_mark = ''
    i = 0
    while i in range(4):
        if code[i] == guess[i]:
            check_mark = check_mark + '● '
            code = code.replace(code[i], ' ',1)
            guess = guess.replace(guess[i], ' ',1)
        i += 1
    for number in code:
        if number ==' ':
            continue
        elif number in guess:
            circle = circle + 'o '
            code = code.replace(number, ' ',1)
            guess = guess.replace(number, ' ',1)
            
    
    clue = circle + check_mark
    return clue


'''3. generates permutations of all the possible combinations. We use this to help solve the game '''

def generate_permutations_with_duplicates(numbers, length, current=''):
    if length == 0:
        return [tuple(current)]

    result = []
    for i in range(len(numbers)):
        result.extend(generate_permutations_with_duplicates(numbers, length-1, current + numbers[i]))

    return result

'''4. get the probability distribution of a particular guess
      the way to do that is assume each code in the list is the real code and then see how many of each different clue is possible
      example: '1234' is the start_code and then we iterate through all the permutations of 1-6, to see how many of clues are possible
       '''

def get_prob_dist(start_code,permutations_list):


    counter =	{
    "● ● ● ● ": 0,
    "● ● ● ": 0,
    "● ● ": 0,
    "● ": 0,
    "o o o o ":0,
    "o o o ":0,
    "o o ":0,
    "o ":0,
    "o o o ● ":0,
    "o o ● ● ":0,
    "o ● ● ● ":0,
    "o o ● ":0,
    "o ● ● ":0,
    "o ● ":0,
    "": 0
    
    }



    total = {}
    for thing in permutations_list:
        code = ''.join(thing)
        x = Clues(code,start_code)
        total[thing] = x
        counter[x] =counter[x]+1

    # print(counter)
    total = sum(counter.values())
    counter = {key: value / total for key, value in counter.items()}


    return counter

'''5. This calculates the amount of information for every code and the possible clues'''

def calculate_info(counter):
    information = {}
    for key,value in counter.items():
        if value != 0:
            information[key] = math.log2(1/value)
        else:
            information[key] = 0


    return information


'''6. This calculates the expected information or the entropy by summing up all the information * probabilities'''

def calculate_expected_information(probabilities):
    sum = 0
    for key,value in probabilities.items():
        if value != 0:
            sum = sum + (value * math.log2(1/value))
        else:
            sum = sum + 0

    return sum

'''7. this is just a for loop for all the codes in a particular list'''

def get_expected_value_for_all(permutations_list):
    total = {}
    for thing in permutations_list:
        input_code = ''.join(thing)
        x = get_prob_dist(input_code,permutations_list)
        expected_value = calculate_expected_information(x)
        total[input_code] = expected_value
    
    return total

''' this is to help us find a key for a given value'''
def find_key(dictionary, value):
    matching_keys = [key for key, val in dictionary.items() if val == value]
    return matching_keys if matching_keys else None



''' 8. this computes the the expected values for all the guesses in a list and then selects the one with the largest expected value'''
def find_next_guess(possible_answers):
    total_guesses = get_expected_value_for_all(possible_answers)
    largest_expected_Value = max(total_guesses.values())
    guess = find_key(total_guesses, largest_expected_Value)
    print(largest_expected_Value)

    return guess[0]



'''9. remove unwanted guesses, by computing the clue and seeing if the clue is the same'''

def remove_unwanted(possible_answers,guess,clue):
    other_list = []
    for thing in possible_answers:
        clue_output = Clues(''.join(thing),guess[0])
        if clue == clue_output:
            other_list.append(thing)
    return other_list






'''10. displays prior guesses'''

def display_guess(guess_code):
    for thing in guess_code:
        a = " ".join(thing)
        
        b = guess_code[thing]
        print(a, '|', b )


'''
Check Guess and select guess
'''

def Guess(total_guesses,possible_answers):
    Guess = ''
    y = False
    while not(len(Guess)==4 and y):  
        print('Numbers to Choose from: ')
        print('1 2 3 4 5 6\n')

        g = []
        Guess = find_next_guess(possible_answers)
        if len(Guess) != 4:
            print('You entered a code that is not 4 digits long')
            print('Please Try Again')
        for item in Guess:
            g.append(item)
        K_guess = tuple(g)
        if K_guess in total_guesses:
            y = False
            print('You have already guesses this Code \n')
            print('Please Try Again')
        else:
            y = True
    h = [Guess,K_guess]
    return h




def play_game():
    total_guesses = {}
    possible_answers = generate_permutations_with_duplicates(['1','2','3','4','5','6'], 4)
    print('')

    print("Let's get started! \n")

    print("Hmmm... I am thinking of a code \n")
    code = choose_code()

    print('Ok! I got one.\n')
 
    guess_num = 0
    while guess_num < 12:      
        print(len(possible_answers))
        guess = Guess(total_guesses,possible_answers)
        possible_answers.remove(guess[1])
        clue = Clues(guess[0],code)
        possible_answers = remove_unwanted(possible_answers,guess,clue)
        
        
        total_guesses[guess[1]] = clue
        guess_num += 1
        if clue == '● ● ● ● ':
            print('Congratulations That was my code')
          
            display_guess(total_guesses)
          
            print('you Guessed it in ', guess_num, ' guesses!')
            break
        else:
            print("Here are your previous Guesses and clues: \n")
            display_guess(total_guesses)
        
            print('You have ', 12 - guess_num, " guesses left \n")
       
            
            continue

    if not(clue == '● ● ● ● '):
        print('You ran out of guesses')
        print('My code was: ', code)


x = play_game()

