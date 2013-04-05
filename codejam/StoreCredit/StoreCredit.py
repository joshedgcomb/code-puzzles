''' This script was written to solve the 'Store Credit' problem from
the 2010 Google Code Jam. The problem description and sample input files
can be found at http://code.google.com/codejam/contest/351101/dashboard#s=p0,
should you wish to run this yourself.

Author: Josh Edgcomb
Last Updated: 4/5/13'''


# solves for a single test case by iterating over the list of item prices
# and checking for solutions. Runs in O(n^2). Not optimal, but works well
# enough on the large input sample.
def solve_single(credit, item_prices):

    for i in range(len(item_prices)):
        current = credit
        current -= item_prices[i]
        for j in range(len(item_prices)):
            if current == item_prices[j] and i != j:
                return '%d %d' % (i+1, j+1)

    return -1


# takes the string of item prices and converts them to a list of ints
def get_item_prices(item_string):

    item_prices = item_string.split(' ')
    for x in range(len(item_prices)):
        item_prices[x] = int(item_prices[x])

    return item_prices


# basic in/out file opening
input_filename = 'A-large-practice.in'
input_file = open(input_filename)
num_cases = int(input_file.readline())
output_filename = 'output.txt'
output_file = open(output_filename, 'w')


# iterates through all test cases and writes solutions to output_file.
# rstrip used on strings to get rid of newline characters, which were
# causing issues
def output():

    for x in range(num_cases):
        credit_string = input_file.readline().rstrip()
        credit = int(credit_string)

        # sample input contains line for number of items, but I don't
        # use it in the solution, so skip over it
        input_file.readline()
        item_string = input_file.readline().rstrip()
        item_prices = get_item_prices(item_string)

        output_file.write('Case #%d: %s\n'
                          % (x+1, solve_single(credit, item_prices)))


output()
