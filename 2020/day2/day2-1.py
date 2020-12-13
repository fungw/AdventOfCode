import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(x)

  return data

def process(data):
  count = 0
  
  for info in data:
    infoRow = info.split(" ")

    range = infoRow[0].split("-")
    min = range[0]
    max = range[1]

    letter = infoRow[1].rstrip(":")
    input = infoRow[2].rstrip()

    count = count + verify(int(min), int(max), letter, input)

  return count


def verify(min, max, letter, input):
  count = input.count(letter)
  if (count >= min and count <= max):
    return 1
  
  return 0


def main():
  data = readFile()
  
  print(process(data))

main()