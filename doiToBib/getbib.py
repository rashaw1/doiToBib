# Main interface that takes either a file with a list of DOIs
# or a single DOI input and returns a bibtex file with their entries
#
# October 2016 Robert Shaw

from converters import *

def GetBib(doi):
    print doiToBib(doi).ToString()

def GetBibs(input_file, output_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    output = open(output_file, 'w')
    for line in lines:
        output.write(doiToBib(line.strip()).ToString())
        output.write("\n\n")
        print "Completed " + line
        
    
