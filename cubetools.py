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
          isFront = 1 if z == 0 else 0
          isBack = 1 if z == n-1 else 0
          rows.append([id, x, y, z, type, isTop, isRight, isBottom, isLeft, isFront, isBack])
          id += 1
  return rows


def fillCubeTable(tbl, n):
  tbl.clear()
  tbl.appendRow(['id', 'x', 'y', 'z', 'type', 'istop', 'isright', 'isbottom', 'isleft', 'isfront', 'isback'])
  rows = generateCubeRows(n)
  for row in rows:
    tbl.appendRow(row)


def generatePathPositionRows(startOffset, n, cubeTbl, axis0 = 'x', axis1 = 'y'):
  rows = []
  parts = [
           ('t', generatePathPositions_TOP_to_RIGHT(startOffset, n)),
           ('r', generatePathPositions_RIGHT_to_BOTTOM(startOffset, n)),
           ('b', generatePathPositions_BOTTOM_to_LEFT(startOffset, n)),
           ('l', generatePathPositions_LEFT_to_TOP(startOffset, n))
          ]
  for part in parts:
    #rows.append([part[0], 'id', getCubeId(cubeTbl, part[1][0], part[1][1], ??????) ])
    (xrow, yrow) = positionsToRows(part[1])
    xrow.insert(0, part[0])
    xrow.insert(1, axis0)
    yrow.insert(0, part[0])
    yrow.insert(1, axis1)
    rows.append(xrow)
    rows.append(yrow)
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

def fillPathPositionTable(tbl, startOffset, n, cubeTbl, axis0 = 'x', axis1 = 'y'):
  tbl.clear()
  rows = generatePathPositionRows(startOffset, n, cubeTbl, axis0, axis1)
  for row in rows:
    tbl.appendRow(row)
def fillPathPositionCHOP(chop, startOffset, n, cubeTbl, axis0 = 'x', axis1 = 'y'):
  parts = [
           ('t', generatePathPositions_TOP_to_RIGHT(startOffset, n)),
           ('r', generatePathPositions_RIGHT_to_BOTTOM(startOffset, n)),
           ('b', generatePathPositions_BOTTOM_to_LEFT(startOffset, n)),
           ('l', generatePathPositions_LEFT_to_TOP(startOffset, n))
          ]
  chop.clear()
  chop.end = len(parts[0][1])-1
  for part in parts:
    ch0 = chop.appendChan(part[0] + axis0)
    ch1 = chop.appendChan(part[0] + axis1)
    xrow, yrow = positionsToRows(part[1])
    #print( part[0] + axis0 + '-> ' + repr(xrow) )
    #print( part[0] + axis1 + '-> ' + repr(yrow) )
    ch0.vals = xrow#[:len(xrow)-1]
    ch1.vals = yrow#[:len(yrow)-1]

def positionsToRows(positions):
  xrow = []
  yrow = []
  for (x,y) in positions:
    xrow.append(x)
    yrow.append(y)
  return (xrow, yrow)

def getCubeId(cubeTbl, x, y, z):
  (x,y,z) = (str(int(x)),str(int(y)),str(int(z)))
  labels = cubeTbl.row(0)
  iid = labels.index('id')
  ix = labels.index('x')
  iy = labels.index('y')
  iz = labels.index('z')
  for row in cubeTbl.rows():
    if row[ix].val == x and row[iy].val == y and row[iz].val == z:
      return row[iid].val





if __name__ == 'main':
  print(repr( generatePathPositions_TOP_to_RIGHT(2, 4) ) )