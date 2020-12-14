import re

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.read()
  for x in fl:
    data.append(x)

  return data

def process(data):
  x = 0
  counter = 1
  for k in data:
    if hex(ord(k)) == "0x28":
      x += 1
    elif hex(ord(k)) == "0x29":
      x -= 1
    if (x == -1):
      print(counter)
    counter += 1
      
  return x

def main():  
  data = readFile()
  print(process(data))

main()