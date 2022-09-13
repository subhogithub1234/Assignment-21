""" 
10. Write a recursive python function to print a number in reverse order.
 """

def fun(n):
    
    if n>0:
      print(n%10,end="")
      fun(n//10)
       
fun(int(input("Enter the number:")))
      