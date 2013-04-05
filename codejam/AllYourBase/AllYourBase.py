''' This script is designed to solve the "All Your Base" problem from the
2009 Google Code Jam. The problem description and sample input files can
be found at http://code.google.com/codejam/contest/189252/dashboard#s=p0,
if you would like to run it yourself.

Author: Josh Edgcomb
Last Updated: 4/5/13
'''


# Solves for a single test case
def solve_single(input_string):

    # rstrip gets rid of newline characters, which were causing issues
    input_string = input_string.rstrip()

    # creates a list of unique characters in order of appearance
    characters = []
    for i in input_string:
        if i not in characters:
            characters.append(i)

    character_values = {}
    for j in range(len(characters)):

        # gives characters values based on order of appearance
        character_values[characters[j]] = j

    # 1 and 0 swapped because instructions state string will never
    # start with 0
    character_values[characters[0]] = 1
    if len(characters) > 1:
        character_values[characters[1]] = 0
        base = len(characters)
    else:
        base = 2

    seconds_until_attack = 0
    multiplier = 1

    # iterates over string from right to left, multipying by base each time
    for i in reversed(input_string):
        seconds_until_attack += character_values[i] * multiplier
        multiplier *= base

    return seconds_until_attack


input_filename = 'A-large-practice.in'
input_file = open(input_filename)
num_cases = int(input_file.readline())
output_filename = 'output.txt'
output_file = open(output_filename, 'w')


# iterates through all test cases and writes solutions to outputFile
def output():

    for x in range(num_cases):
        input_string = input_file.readline()
        output_file.write('Case #%d: %d\n' % (x+1, solve_single(input_string)))


output()
