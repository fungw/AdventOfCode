import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(x.rstrip())

  return data

def process(data, right, down):
  treeCount = 0
  xPos = 0
  yPos = 0

  for z in range(len(data)):
    for y in range(right):
      xPos = xPos + 1
      try:
        access = data[yPos][xPos]
      except IndexError:
        xPos = 0
    for x in range(down):
      yPos = yPos + 1
      try:
        access = data[yPos][xPos]
        if (data[yPos][xPos] == '#' and x == down-1):
          treeCount = treeCount + 1
      except IndexError:
        return treeCount

  return treeCount

def main():
  data = readFile()
  
  print(process(data, 1, 1))
  print(process(data, 3, 1))
  print(process(data, 5, 1))
  print(process(data, 7, 1))
  print(process(data, 1, 2))

  print(process(data, 1, 1)
    * process(data, 3, 1)
    * process(data, 5, 1)
    * process(data, 7, 1)
    * process(data, 1, 2))

main()