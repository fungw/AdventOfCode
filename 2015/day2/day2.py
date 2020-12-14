def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(x.strip().split('x'))

  return data

def calculateWrappingPaper(data):
  result = 0
  for x in data:
    length = int(x[0]) * int(x[1])
    width = int(x[1]) * int(x[2])
    height = int(x[2]) * int(x[0])
    extra = min(length, width, height)

    result += extra + length*2 + width*2 + height*2
  return result

def calculateRibbon(data):
  result = 0
  for x in data:
    perimeter1 = int(x[0])*2 + int(x[1])*2
    perimeter2 = int(x[1])*2 + int(x[2])*2
    perimeter3 = int(x[0])*2 + int(x[2])*2
    perimeter = min(perimeter1, perimeter2, perimeter3)
    extra = int(x[0]) * int(x[1]) * int(x[2])
    result += perimeter + extra
  return result

def main():  
  data = readFile()
  print(calculateWrappingPaper(data))
  print(calculateRibbon(data))

main()