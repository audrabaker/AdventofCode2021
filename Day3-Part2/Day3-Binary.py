import sys
import itertools

def recursiveSortLess(Line, commonA, commonB, c):
  ones = zeros = 0
  for line in Line:
    if line[c] == 1:
      commonA[ones] = line
      ones += 1
    else:
      commonB[zeros] = line
      zeros += 1

  for i in itertools.islice(commonA, zeros, len(commonA) - 1):
    commonA[i] = 0

  for i in itertools.islice(commonB, zeros, len(commonB) - 1):
    commonB[i] = 0


  if ones >= zeros:
    if c < len(commonA[0]):
      recursiveSortLess(commonA, commonA, commonB, c+1)
    return(commonA, commonB)
  elif c < len(commonB[0]):
    recursiveSortLess(commonB, commonA, commonB, c+1)
  return(commonB, commonA)


n = len(sys.argv)
if (n < 2): 
  print("No file provided. Try again")
  sys.exit(0)
try:
  file = open(sys.argv[1], 'r')
except FileNotFoundError:
  print("File not found")

Line = file.readlines()
for i in Line:
  

commonA = [0] *(len(Line[0]))
commonB = [0] *(len(Line[0]))
Most,Less = recursiveSortLess(Line, commonA, commonB, 0)

print(Most)
print(Less)
