import csv
import re

def readFile():
  data = []
  with open('data.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for x in readCSV:
      data.append(x)
  return data[0]

def process(data):
  dataset = data

  for idx, num in enumerate(dataset):
    if (idx % 4 == 0):
      if (re.match(num, '1')):
        dataset = add(dataset, idx)
      elif (re.match(num, '2')):
        dataset = multiple(dataset, idx)
      elif (re.match(num, '99')):
        break
      else:
        raise Exception('No INSTRUCTION found')
  return dataset

def add(data, idx):
  xPos = data[idx+1]
  yPos = data[idx+2]

  xVal = data[int(xPos)]
  yVal = data[int(yPos)]

  result = int(xVal) + int(yVal)

  resultPos = data[idx+3]
  data[int(resultPos)] = str(result)

  return data

def multiple(data, idx):
  xPos = data[idx+1]
  yPos = data[idx+2]

  xVal = data[int(xPos)]
  yVal = data[int(yPos)]

  result = int(xVal) * int(yVal)

  resultPos = data[idx+3]
  data[int(resultPos)] = str(result)

  return data

def main():  
  data = readFile()
  i = 0

  while i <= 99:
    j = 0
    dataset = data.copy()
    while j <= 99:
      dataset[1] = str(i)
      dataset[2] = str(j)

      processedResult = process(dataset)
      if (int(processedResult[0]) == 19690720):
        result = 100 * i + j
        print(result)
      j += 1
      dataset = data.copy()
    i += 1

main()