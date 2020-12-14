def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.read()
  for x in fl:
    data.append(x)

  return data

def create2dArray(x, y):
  rows, cols = (x, y)
  arr = [[0 for i in range(cols)] for j in range(rows)]
  return arr

def route(data, array, arrayCenter, arraySize):
  array[arrayCenter][arrayCenter] += 1

  for x in data:
    print(hex(ord(x)))
  return array

def main():
  data = readFile()

  arraySize = 100
  arrayCenter = arraySize/2
  array = create2dArray(arraySize, arraySize)

  route(data, array, arrayCenter, arraySize)

main()