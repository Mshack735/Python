# Don't delete any of the given code.
def maxBlock(string):
  # insert your logic here
  block=0
  total=0
  for x in range(len(string)):
    letter=string[x]
    if x == 0:
      sameletter=string[x]
    if sameletter!=letter:
      sameletter=letter
      if block>total:
        total=block
      block=0
    if letter==sameletter:
      block+=1
  if block>total:
    total=block
  return total
      
    
  
# Test cases. Don't modify  
print(1,maxBlock("hoopla"))	         # this would be 2
print(2,maxBlock("abbCCCddBBBxx"))	 # this would be 3
print(3,maxBlock(""))	               # this would be 0
print(4,maxBlock("xyz"))	
print(5,maxBlock("xxyz"))	
print(6,maxBlock("xyzz"))	
print(7,maxBlock("abbbcbbbxbbbx"))	
print(8,maxBlock("XXBBBbbxx"))	
print(9,maxBlock("XXBBBBbbxx"))	
print(10,maxBlock("XXBBBbbxxXXXX"))
print(11,maxBlock("XX2222BBBbbXX2222"))
