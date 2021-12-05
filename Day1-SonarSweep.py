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

count = 0
firstpass = 1
 
for line in Line:
  if not firstpass:
    if last < line:
      count += 1
      print(f'{last} {line}: {count}')
  last = line
  firstpass = 0 

print(f"Number of increases is: {count}")
file.close()

  
