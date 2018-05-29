import collections
from collections import Counter
import statistics
numbers= input('Input your list of numbers:')
number=[ int(x) for x in numbers.split(" ") ]
print('')
mean=0
for x in range(len(number)):
  mean+=number[x]
print('mean:', mean/len(number))


values = sorted(number)
if len(number)%2 ==1:
  print('median:',values[len(values)//2])
if len(number)%2 ==0:
  print('median:',values[(len(values)-1)//2],values[(len(values))//2])  


def mode(numbers):
    largestCount = 0
    modes = []
    for x in numbers:
        if x in modes:
            continue
        count = numbers.count(x)
        if count > largestCount:
            del modes[:]
            modes.append(x)
            largestCount = count
        elif count == largestCount:
            modes.append(x)
    return modes

try: 
  x= (mode(number)[0])
  print('mode:',x)
  
except statistics.StatisticsError:
  print('mode: no mode')
