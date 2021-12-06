# set up python environment 
import os
import sys

# main function
def main():
  # get input from input.txt
  input_file = open("input.txt", "r")

  # counter starting at 0
  counter = 0

  # define last value
  lastValue = None

  #iterate through input file and keep track of current position 
  for line in input_file:
    if (lastValue is None):
      print(line + " No previous value") 
    elif (lastValue < int(line)):
      print(line + "(increased)")
      counter += 1
    else:
      print(line + "(decreased)")  
    lastValue = int(line)

  print("Number of increases: " + str(counter))

if __name__ == '__main__':
    main()