""" 
9. Write a recursive python function to print first N multiples of a given number.
 """

def fun1(n):
    if n>0:
      fun1(n-2)
      
      print(n,end=",")

x=int(input("Enter the number:"))
fun1(x)
