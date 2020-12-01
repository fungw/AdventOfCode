import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(int(x))

  return data

def find(data):
  matchVal = 2020
  pivotCount = 0
  while pivotCount < len(data) - 2:
    pivot = data[pivotCount]
    matchCount = pivotCount + 1
    while matchCount < len(data) - 1:
      match = data[matchCount]
      tripleCount = matchCount + 1
      while tripleCount < len(data):
        tripleMatch = data[tripleCount]
        if pivot + match + tripleMatch == matchVal:
          return pivot * match * tripleMatch
        tripleCount += 1
      matchCount += 1
    pivotCount += 1

  return 0

def main():  
  data = readFile()
  print(find(data))

main()