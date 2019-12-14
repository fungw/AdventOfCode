DATA_START = 183564
DATA_END = 657474

def sixDigitNumber(number):
  return len(str(number)) == 6

def adjacentNumber(number):
  counter = 0
  adjacentMatch = False
  stringified = str(number)
  
  while counter < len(stringified) - 1:
    if stringified[counter] == stringified[counter+1]:
      adjacentMatch = True
    counter += 1
  
  return adjacentMatch

def nonDecreasing(number):
  counter = 0
  nonDecreasing = True
  stringified = str(number)

  while counter < len(stringified) - 1:
    if not stringified[counter] <= stringified[counter+1]:
      nonDecreasing = False
    counter += 1
  
  return nonDecreasing

def adjacentNumberExtended(number):
  counter = 0
  matchCount = 0
  adjacentNumberLengths = []
  stringified = str(number)
  
  while counter < len(stringified) - 1:
    if stringified[counter] == stringified[counter+1]:
      matchCount += 1
    else:
      if matchCount > 0:
        adjacentNumberLengths.append(matchCount)
      matchCount = 0
    counter += 1

  if (matchCount == 1):
    adjacentNumberLengths.append(matchCount)
  
  return 1 in adjacentNumberLengths

def main():
  counter = DATA_START
  passwordCount = 0
  while (counter <= DATA_END):
    if sixDigitNumber(counter) and adjacentNumber(counter) and nonDecreasing(counter) and adjacentNumberExtended(counter):
      passwordCount += 1
    counter += 1
  print("Password count:", passwordCount)

main()