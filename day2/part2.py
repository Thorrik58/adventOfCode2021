# set up python environment 
import os
import sys

# main function
def main():
  # get input from input.txt
  input_file = open("input.txt", "r")

  # horizontal position
  horizontal_pos = 0

  # depth position
  vertical_pos = 0

  aim = 0

  #iterate through input file and keep track of increases 
  for line in input_file:
    # split line on whitespace
    line = line.split()
    if (line[0] == "up"):
      aim -= int(line[1])
    if (line[0] == "down"):
      aim += int(line[1])
    if (line[0] == "forward"):
      horizontal_pos += int(line[1])
      vertical_pos += aim * int(line[1])

  print(horizontal_pos * vertical_pos)


if __name__ == '__main__':
    main()