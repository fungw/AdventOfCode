import math

def readFile():
  f = open("data.txt", "r")
  data = []

  fl = f.readlines()

  output = []
  for x in fl:
    if (len(output) == 0):
      output = x.rstrip()
    else:
      output = output + ' ' + x.rstrip()

    if (x == '\n'):
      data.append(output.rstrip())
      output = []

  data.append(output.rstrip())
  return data

def process(passports):
  count = 0

  for passport in passports:
    mapping = {
      "byr": 0,
      "iyr": 0,
      "eyr": 0,
      "hgt": 0,
      "hcl": 0,
      "ecl": 0,
      "pid": 0,
    }

    fields = passport.split(' ')
    for field in fields:
      attribute = field.split(':')
      if (attribute[0] != 'cid'):
        mapping[attribute[0]] = mapping[attribute[0]] + 1
    
    if (verify(mapping) == True):
      count = count + 1

  return count

def verify(data):
  for key, value in data.items():
    if (value == 0):
      return False
  
  return True

def main():
  passports = readFile()

  print(process(passports))

main()