""" 
1. Write a recursive python function to print first N natural numbers.
 """



def fun1(n):
    if n>0:
       fun1(n-1) 
       print(n,end=" ")
      
fun1(int(input("Enter the value of N:")))       

#=====================================OUTPUT================================

# Enter the value of N:10
# 1 2 3 4 5 6 7 8 9 10 