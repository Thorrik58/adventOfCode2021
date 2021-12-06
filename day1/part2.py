# set up python environment 
import os
import sys

# main function
def main():
  # get input from input.txt
  input_file = open("input.txt", "r")

  isFirstRun = True
  increaseCounter = 0
  lastSumValue = None

  # create list to store values
  valuesFirst = []
  valuesSecond = []

  # iterate through input file and keep track of current position 
  for line in input_file:
    # Case for first run, there is a smarter way to do this but let's do it this way for now
    if (isFirstRun):
      valuesFirst.append(int(line))
      isFirstRun = False
    else:
      valuesFirst.append(int(line))
      valuesSecond.append(int(line))

    if (lastSumValue != None):
      if (lastSumValue < sum(valuesFirst)):
        print("Increased")
        increaseCounter += 1
      else:
        print("Decreased")
      
    # just to make sure we dont start summing up until we have 3 values in the list
    if (len(valuesFirst) == 3):
      lastSumValue = sum(valuesFirst)
      valuesFirst=valuesSecond
      valuesSecond=[int(line)]

  print("Number of increases: " + str(increaseCounter))

if __name__ == '__main__':
    main()