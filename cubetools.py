# cubetools.py


def generateCubeRows(n):
  rows = []
  n = int(n)
  id = 0
  for z in range(0, n):
    for y in range(0, n):
      for x in range(0, n):
        maxed = 0
        for c in (x,y,z):
          if c==(n-1) or c==0:
            maxed = maxed + 1
        if maxed > 0:
          if maxed == 1:
            type = 'face'
          elif maxed == 2:
            type = 'edge'
          elif maxed == 3:
            type = 'corner'
          isTop = 1 if y == n-1 else 0
          isBottom = 1 if y == 0 else 0
          isLeft = 1 if x == 0 else 0
          isRight = 1 if x == n-1 else 0
          rows.append([id, x, y, z, type, isTop, isBottom, isLeft, isRight])
          id += 1
  return rows


def fillCubeTable(tbl, n):
  tbl.clear()
  tbl.appendRow(['id', 'x', 'y', 'z', 'type', 'istop', 'isright', 'isbottom', 'isleft'])
  rows = generateCubeRows(n)
  for row in rows:
    tbl.appendRow(row)


def generatePathPositionRows(startOffset, n, axis0 = 'x', axis1 = 'y'):
  rows = []
  parts = [
           ('t', generatePathPositions_TOP_to_RIGHT(startOffset, n)),
           ('r', generatePathPositions_RIGHT_to_BOTTOM(startOffset, n)),
           ('b', generatePathPositions_BOTTOM_to_LEFT(startOffset, n)),
           ('l', generatePathPositions_LEFT_to_TOP(startOffset, n))
          ]
  for part in parts:
    rows.extend(positionsToRows(part[1], part[0], axis0, axis1))
  return rows

def generatePathPositions_TOP_to_RIGHT(startOffset, n):
  positions = []
  (x,y) = (startOffset, n-1)
  positions.append( (x,y) )
  y += 1
  positions.append( (x,y) )
  while x <= (n - 1):
    x += 1
    positions.append( (x,y) )
  while y >= (n-startOffset):
    y -= 1
    positions.append( (x,y) )
  x -= 1
  positions.append( (x,y) )
  return positions

def generatePathPositions_RIGHT_to_BOTTOM(startOffset, n):
  positions = []
  (x,y) = (n-1, n-1-startOffset)
  positions.append( (x,y) )
  x += 1
  positions.append( (x,y) )
  while y > -1:
    y -= 1
    positions.append( (x,y) )
  while x >= (n-startOffset):
    x -= 1
    positions.append( (x,y) )
  y += 1
  positions.append( (x,y) )
  return positions

def generatePathPositions_BOTTOM_to_LEFT(startOffset, n):
  positions = []
  (x,y) = (n-1-startOffset, 0)
  positions.append( (x,y) )
  y -= 1
  positions.append( (x,y) )
  while x > -1:
    x -= 1
    positions.append( (x,y) )
  while y < startOffset:
    y += 1
    positions.append( (x,y) )
  x += 1
  positions.append( (x,y) )
  return positions

def generatePathPositions_LEFT_to_TOP(startOffset, n):
  positions = []
  (x,y) = (0, startOffset)
  positions.append( (x,y) )
  x -= 1
  positions.append( (x,y) )
  while y < n:
    y += 1
    positions.append( (x,y) )
  while x < startOffset:
    x += 1
    positions.append( (x,y) )
  y -= 1
  positions.append( (x,y) )
  return positions

def fillPathPositionTable(tbl, startOffset, n, axis0 = 'x', axis1 = 'y'):
  tbl.clear()
  rows = generatePathPositionRows(startOffset, n, axis0, axis1)
  for row in rows:
    tbl.appendRow(row)

def positionsToRows(positions, name, axis0 = 'x', axis1 = 'y'):
  xrow = [name, axis0]
  yrow = [name, axis1]
  for (x,y) in positions:
    xrow.append(x)
    yrow.append(y)
  return (xrow, yrow)

if __name__ == 'main':
  print(repr( generatePathPositions_TOP_to_RIGHT(2, 4) ) )