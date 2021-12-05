import sys

n = len(sys.argv)
if (n < 2):
  print("No file provided. Try again")
  sys.exit(0)
try:
  file = open(sys.argv[1], 'r')
except FileNotFoundError:
  print("File not found")

Line = map(int, file.readlines())

increasing = 0
currentLineNo = 0
 
for line in Line:
  #check to see if this is our first couple of lines
  if currentLineNo == 0:
    lineA = line
  if currentLineNo == 1:
    lineB = lineA
    lineA = line
  if currentLineNo == 2:
    curMeasure = lineB + lineA + line
    lineC = lineB
    lineB = lineA
    lineA = line
  if currentLineNo > 2:
    prevMeasure = curMeasure
    lineC = lineB
    lineB = lineA
    lineA = line
    curMeasure = lineA + lineB + lineC
    if prevMeasure < curMeasure:
      increasing += 1
      print(f'{prevMeasure} {curMeasure}: {increasing}')
  currentLineNo += 1
print(f"Number of increases is: {increasing}")
file.close()

  
