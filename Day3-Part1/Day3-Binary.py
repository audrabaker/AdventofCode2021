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

powerConsumption = 0
gammaRate = 0
epsilonRate = 0



numbers = []

for line in Line:  
  entry = list(line.strip())
  for i in entry:
    print(i)
    count = 1 
    if i == '1':
      print(i + " " + str(count))
      numbers[count] += 1
      print(loop)
    count += 1

print("My numbers are: ")
print(*numbers)  



 

