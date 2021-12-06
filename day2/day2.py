# set up python environment 
import os
import sys

# main function
def main():
  # get input from input.txt
  input_file = open("input.txt", "r")

  # counter starting at 0
  counter = 0

  # counter of increases
  increaseCounter = 0

  # define last value
  lastValue = None

  # lastSumValue set to None 
  lastSumValue = None

  compareNextRun = False

  # create list to store values
  valuesFirst = []
  valuesSecond = []
  valuesThird = []

  # iterate through input file and keep track of current position 
  for line in input_file:
    # Case for first three runs, there is a smarter way to do this but let's do it this way for now
    if (counter == 0):
      valuesFirst.append(int(line))
    else:
      valuesFirst.append(int(line))
      valuesSecond.append(int(line))

    if (lastSumValue != None):
      if (lastSumValue < sum(valuesFirst)):
        print("Increased")
        increaseCounter += 1
      else:
        print("Decreased")
      
    # if every third run
    if (len(valuesFirst) == 3):
      lastSumValue = sum(valuesFirst)
      valuesFirst=valuesSecond
      valuesSecond=[int(line)]

    counter += 1
  print("Number of increases: " + str(increaseCounter))

if __name__ == '__main__':
    main()