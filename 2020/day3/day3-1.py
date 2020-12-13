import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(x.rstrip())

  return data

def process(data):
  treeCount = 0
  xPos = 0
  yPos = 0

  for z in range(len(data)):
    for y in range(3):
      xPos = xPos + 1
      try:
        access = data[yPos][xPos]
      except IndexError:
        xPos = 0
    for x in range(1):
      yPos = yPos + 1
      try:
        access = data[yPos][xPos]
        if (data[yPos][xPos] == '#'):
          treeCount = treeCount + 1
      except IndexError:
        return treeCount

  return treeCount

def main():
  data = readFile()
  
  print(process(data))

main()