# write a python script to write the execution time for
# a variable in a file when the variable is used to find
# factorial using iterative & recursion method

import timeit
file = open("time_comp.txt", "w")
for no in range(5, 950 ,5):
   #***************Recursion*****************
   
   start = timeit.timeit()
   fac = 1
   if no < 0:
       print("factorial not exist")
   elif no == 0:
       print("The factorial of 0 is 1")
   else:
       for i in range(1, no + 1):
           fac = fac*i
   end = timeit.timeit()
   time = str(end - start)
   p = ("The factorial of "+str(no)+" is "+str(fac)+" by Recursive Method")
   file.write(p+"\n"+time + " Sec "+"\n")

   #**************Iteration*****************
   start_2 = timeit.timeit()
   def fact(x):
       if(x == 0 or x == 1):
           y = 1
           return (y)
       else:
           y = x*fact(x-1)
           return (y)

   funct_val = fact(no)
   end_2 = timeit.timeit()
   time_2 = str(end_2 - start_2)
   p2 = ("factorial of " + str(no) + " is " + str(funct_val) + " by Iterative Method")
   file.write(p2+"\n"+time_2+"Sec"+"\n")
file.close()
