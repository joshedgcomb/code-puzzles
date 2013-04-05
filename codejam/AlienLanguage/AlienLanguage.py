''' This script was written to solve the 'Alien Language' problem from
the 2009 Google Code Jam. The problem description and sample input files 
can be found at http://code.google.com/codejam/contest/90101/dashboard#s=p0,
should you wish to run this yourself.'''


inputFilename = 'A-small-practice.in'
inputFile = open(inputFilename)
outputFilename = 'output.txt'
outputFile = open(outputFilename)
parameter_string = (inputFile.readline()).rstrip()
parameter_list = parameter_string.split(' ')

word_length = int(parameter_list[0])
num_known_words = int(parameter_list[1])
num_cases = int(parameter_list[2])

known
