import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(int(x))

  return data

def calculateFuel(data):
  result = data
  
  result = [i / 3 for i in result]
  result = [math.floor(j) for j in result]
  result = [k - 2 for k in result]

  return result

def sumOfFuel(data):
  resultSum = 0
  for l in data:
    resultSum += l

  return resultSum

def calculateFuelOfFuel(data):
  fuel = data

  fuel /= 3
  fuel = math.floor(fuel)
  fuel -= 2

  if (fuel < 0):
    return 0

  return fuel + calculateFuelOfFuel(fuel)

def fuelOfFuel(data):
  result = []
  for x in data:
    result.append(calculateFuelOfFuel(x))
  return result

def main():  
  data = readFile()
  print("Day 1-1:", sumOfFuel(calculateFuel(data)))
  print("Day 1-2:", sumOfFuel(fuelOfFuel(data)))

main()