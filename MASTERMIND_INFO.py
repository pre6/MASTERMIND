
import random
import matplotlib.pyplot as plt
import math


'''
1. get all possible combination
2. get a list of all the possible clues
3. for each possible input
    3b. iterate through all the possible inputs then count all the possible clues possible
    3c. graph it
'''
# inuputis the code and the guess and output the clue
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



# create list of all the possible answers


def generate_permutations_with_duplicates(numbers, length, current=''):
    if length == 0:
        return [tuple(current)]

    result = []
    for i in range(len(numbers)):
        result.extend(generate_permutations_with_duplicates(numbers, length-1, current + numbers[i]))

    return result



permutations_list = generate_permutations_with_duplicates(['1','2','3','4','5','6'], 4)

# there are 6^4 = 1296 possibilities




def get_prob_dist(start_code):


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



    # Sort the dictionary by values in descending order
    sorted_data = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

    # # Extract sorted keys and values from the dictionary
    x_values = list(sorted_data.keys())
    y_values = list(sorted_data.values())

    # Create a bar plot with vertical x-axis labels
    plt.bar(x_values, y_values)
    plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically

    # # Add labels and title
    plt.xlabel('X-axis (Keys)')
    plt.ylabel('Y-axis (Values)')
    plt.title('DIst of ' + start_code)

    # Show the plot
    plt.show()
    return counter


x = get_prob_dist('1225')


print(x)




'''

def calculate_info(counter):
    information = {}
    for key,value in counter.items():
        if value != 0:
            information[key] = math.log2(1/value)
        else:
            information[key] = 0


    return information

y = calculate_info(x)

print(y)


def calculate_expected_information(probabilities):
    sum = 0
    for key,value in probabilities.items():
        if value != 0:
            sum = sum + (value * math.log2(1/value))
        else:
            sum = sum + 0

    return sum
    
print(calculate_expected_information(x))


def get_expected_value_for_all():
    permutations_list = generate_permutations_with_duplicates(['1','2','3','4','5','6'], 4)
    total = {}
    for thing in permutations_list:
        input_code = ''.join(thing)
        x = get_prob_dist(input_code)
        expected_value = calculate_expected_information(x)
        total[input_code] = expected_value
    
    return total

print('start')
y = get_expected_value_for_all()

print(y)

p = max(y.values())
print(p)



def find_key(dictionary, value):
    matching_keys = [key for key, val in dictionary.items() if val == value]
    return matching_keys if matching_keys else None


# Find the key for the given value

result_keys = find_key(y, p)

# Print the result
if result_keys is not None:
    print(f'The keys for value {p} are: {result_keys}')
else:
    print(f'No keys found for value {p}')

sorted_data = dict(sorted(y.items(), key=lambda item: item[1], reverse=True))

# Extract sorted keys and values from the dictionary
x_values = list(sorted_data.keys())
y_values = list(sorted_data.values())

# Create a bar plot with vertical x-axis labels
plt.bar(x_values, y_values)
plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically

# # Add labels and title
plt.xlabel('X-axis (Keys)')
plt.ylabel('Y-axis (Values)')
plt.title('distribusion')

# Show the plot
plt.show()



# def get_new_guess(possible_values, guess):
#     # 1. 
'''
    
