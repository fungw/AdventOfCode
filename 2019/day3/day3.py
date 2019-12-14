import math
BIGGRID = 17500
SMALLGRID = 500
DOWN = 'D'
EMPTY = ''
LEFT = 'L'
RIGHT = 'R'
ROUTE1ID = 'route1'
ROUTE2ID = 'route2'
UP = 'U'

def readFile():
  f = open("data.txt", "r")
  dataRouteOne = []
  dataRouteTwo = []

  fl = f.readlines()
  route1 = fl[0].split(",")
  route2 = fl[1].split(",")
  for x in route1:
    dataRouteOne.append(x.strip('\n'))
  for y in route2:
    dataRouteTwo.append(y.strip('\n'))

  return dataRouteOne, dataRouteTwo

def create2dArray(size):
  rows, cols = (size, size)
  arr = [[0 for i in range(cols)] for j in range(rows)]
  return arr

def move(grid, symbol, distance, xpos, ypos, route):
  counter = 0

  while (counter < distance):
    if (symbol == DOWN):
      xpos += 1
      if not (grid[xpos][ypos] == 1 and route == ROUTE1ID):
        if not (grid[xpos][ypos] == 2 and route == ROUTE2ID):
          grid[xpos][ypos] += 1
    if (symbol == LEFT):
      ypos -= 1
      if not (grid[xpos][ypos] == 1 and route == ROUTE1ID):
        if not (grid[xpos][ypos] == 2 and route == ROUTE2ID):
          grid[xpos][ypos] += 1
    if (symbol == RIGHT):
      ypos += 1
      if not (grid[xpos][ypos] == 1 and route == ROUTE1ID):
        if not (grid[xpos][ypos] == 2 and route == ROUTE2ID):
          grid[xpos][ypos] += 1
    if (symbol == UP):
      xpos -= 1
      if not (grid[xpos][ypos] == 1 and route == ROUTE1ID):
        if not (grid[xpos][ypos] == 2 and route == ROUTE2ID):
          grid[xpos][ypos] += 1
    counter += 1
  return [grid, xpos, ypos]

def process(data, array):
  dataset = data
  grid = array
  xpos = math.floor(len(array)/2)
  ypos = 0
  grid[xpos][ypos] = 1
  routeID = ROUTE1ID
  
  for route in dataset:
    for direction in route:
      symbol = direction[0]
      distance = int(direction.replace(symbol, EMPTY))
      [grid, xpos, ypos] = move(grid, symbol, distance, xpos, ypos, routeID)
    routeID = ROUTE2ID
    xpos = math.floor(len(array)/2)
    ypos = 0

  return grid

def calculateManhattan(array):
  xCounter = yCounter = 0
  xpos = math.floor(len(array)/2)
  ypos = 0
  result = 0

  while (xCounter < len(array)):
    while (yCounter < len(array)):
      if (array[xCounter][yCounter] > 1):
        distanceA = abs(xpos - xCounter)
        distanceB = abs(ypos - yCounter)
        distance = distanceA + distanceB
        if (distance < result or result == 0):
          result = distance
      yCounter += 1
    xCounter += 1
    yCounter = 0
  return result

def intersectionLookupByRoute(array, route):
  print(route)
  xpos = math.floor(len(array)/2)
  ypos = 0
  distanceCounter = 0
  pathDistances = {}

  for path in route:
    symbol = path[0]
    distance = int(path.replace(symbol, EMPTY))
    counter = 0
    while (counter < distance):
      distanceCounter += 1
      if (symbol == DOWN):
        xpos += 1
      if (symbol == LEFT):
        ypos -= 1
      if (symbol == RIGHT):
        ypos += 1
      if (symbol == UP):
        xpos -= 1
      if (array[xpos][ypos] == 2):
        hashedLocation = hash(xpos + ypos)
        pathDistances[hashedLocation] = distanceCounter
      counter += 1
  
  return pathDistances

def printGrid(array):
  f=open("output.txt", "a+")
  f.write('\n'.join([' '.join([str(cell) for cell in row]) for row in array]))
  f.close()

def main():
  data = readFile()

  array = create2dArray(BIGGRID)
  array = process(data, array)

  manhattanResult = calculateManhattan(array)
  print("Closest intersection:", manhattanResult)

  pathOneDistances = intersectionLookupByRoute(array, data[0])
  pathTwoDistances = intersectionLookupByRoute(array, data[1])
  print("Intersections:", pathOneDistances, pathTwoDistances)

  shortestSteps = 0
  for key in pathOneDistances:
    totalDistances = pathOneDistances[key] + pathTwoDistances[key]

    if shortestSteps == 0 or totalDistances < shortestSteps:
      shortestSteps = totalDistances

  print("Shortest steps route:", shortestSteps)

main()