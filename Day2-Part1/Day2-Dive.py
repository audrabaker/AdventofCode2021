import sys 

n = len(sys.argv)
if (n < 2): 
  print("No file provided. Try again")
  sys.exit(0)
try:
  file = open(sys.argv[1], 'r')
except FileNotFoundError:
  print("File not found")

Line = file.readlines()

horizontal = 0
depth = 0

for line in Line:
  direction = line.split(" ")
  if direction[0] == 'forward':
    horizontal += int(direction[1])
  elif direction[0] == 'down':
    depth += int(direction[1])
  elif direction[0] == 'up':
    depth -= int(direction[1])

print("The position of the sub is: " + str(depth * horizontal))
