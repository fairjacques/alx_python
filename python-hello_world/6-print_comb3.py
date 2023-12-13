for a in range (10):
    for b in range(a+1,10):
      if a*10+b <89:
        print("{:02}".format(a*10+b),end=", ")
      else:
        print("{:0}".format(a*10+b))