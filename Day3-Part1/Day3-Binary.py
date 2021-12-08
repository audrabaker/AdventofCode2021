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
gammaRate = '0'
epsilonRate = '0'


totalLines = 0
numbers = [0]*(len(Line[0])-1)

for line in Line:  
  totalLines += 1
  entry = list(line.strip())
  print(*entry)
  count = 0
  for i in entry:
    if i == '1':
      numbers[count] += 1
    count += 1

print("My numbers are: ")
print(numbers)  

for i in numbers:
  if totalLines - i > i :
    gammaRate += '0'
    epsilonRate += '1'
  else:
    gammaRate += '1'
    epsilonRate += '0'



print("gamma rate is: ")
print(int(gammaRate,2))
print("\n epsilon rate is: ")
print(int(epsilonRate,2))
print("\n Power consumption is: ")
print(int(gammaRate,2)*int(epsilonRate,2))


 

