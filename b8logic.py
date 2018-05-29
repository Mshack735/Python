# Don't delete any of the given code.

def countYZ(strings):
  # insert your logic here
  numofYZ=0
  for x in range(len(strings)):
    if x+1==len(strings):
      if strings[x]=='y' or strings[x]=='z' or strings[x]=='Y' or strings[x]=='Z':
        numofYZ+=1
    elif strings[x].isalpha():
      continue
    else:
      if strings[x-1]=='y' or strings[x-1]=='z' or strings[x-1]=='Y' or strings[x-1]=='Z':
        numofYZ+=1
    
  return numofYZ
# Test cases. Don't modify  
print(1,countYZ("fez day"))   # this would be 2
print(2,countYZ("day fez"))   # this would be 2
print(3,countYZ("day fyyyz"))   # this would be 2
print(4,countYZ("day yak"))    # this would be 1
print(5,countYZ("day:yak"))
print(6,countYZ("!!day--yaz!!"))
print(7,countYZ("yak zak"))
print(8,countYZ("DAY abc XYZ"))
print(9,countYZ("aaz yyz my"))
print(10,countYZ("y2bz"))
print(11,countYZ("zxyx"))
