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

    positions = infoRow[0].split("-")
    posX = positions[0]
    posY = positions[1]

    letter = infoRow[1].rstrip(":")
    input = infoRow[2].rstrip()

    if (verify(int(posX) - 1, int(posY) - 1, letter, input) == True):
      count = count + 1

  return count

def verify(posX, posY, letter, input):
  result = 0

  if (input[posX] == letter):
    result = result + 1

  if (input[posY] == letter):
    result = result + 1

  return result == 1

def main():
  data = readFile()
  
  print(process(data))

main()