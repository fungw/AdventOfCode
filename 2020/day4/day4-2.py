import math
import re

def readFile():
  f = open("data_validPassports.txt", "r")
  data = []

  fl = f.readlines()
  for x in fl:
    data.append(x.rstrip())

  return data

def dateCheck(value, min, max):
  return len(value) == 4 and int(value) >= min and int(value) <= max

def eclCheck(value):
  return value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'

def hairCheck(value):
  if (value[0] != '#' or len(value) != 7):
    return False

  match = re.search('^#[(a-f0-9)]{6}$', value)
  if match is not None:
    return True
  else:
    return False
  

def heightCheck(value):
  if (len(value) <= 2):
    return False

  metric = value[-2:]
  amount = int(value[:-2])

  if (metric == 'cm'):
    return amount >= 150 and amount <= 193
  
  if (metric == 'in'):
    return amount >= 59 and amount <= 76

  return False

def pidCheck(value):
  return len(value) == 9

def process(passports):
  count = 0

  for passport in passports:
    fields = passport.split(" ")
    result = True
    for field in fields:
      attribute = field.split(":")
      label = attribute[0]
      value = attribute[1]

      if (label == 'byr'):
        result = result * dateCheck(value, 1920, 2002)

      if (label == 'iyr'):
        result = result * dateCheck(value, 2010, 2020)

      if (label == 'eyr'):
        result = result * dateCheck(value, 2020, 2030)

      if (label == 'hgt'):
        result = result * heightCheck(value)

      if (label == 'hcl'):
        result = result * hairCheck(value)

      if (label == 'ecl'):
        result = result * eclCheck(value)

      if (label == 'pid'):
        result = result * pidCheck(value)

    if (result == 1):
      count = count + 1

  return count

def main():
  passports = readFile()
  
  print(process(passports))

main()