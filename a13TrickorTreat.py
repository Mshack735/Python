
def hundred():
  for num in range(1,101):
    if not num%15:
      print('Trick or Treat')
    elif not num%3:
      print('Trick')
    elif not num%5:
      print('Treat')
    else:  
      print(num)
    
hundred()
