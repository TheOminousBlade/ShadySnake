ans = False
while ans != True:
  inp = input("enter a number: ")
  try: 
      inpT = int(inp)  
      for i in range(10):
        newval = int(inp) * inpT
        print(inpT + "^" + i  + "\t" + newval)
        i+1
        inp = newval
      ans = True
  except:
    print("Let's start by picking a simple number...\n")