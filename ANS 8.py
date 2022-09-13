""" 
8. Write a recursive python function to print cubes of first N natural numbers
 """
def fun1(n):
    if n>0:

       fun1(n-1) 
       print(n**3,end=" ")
      
fun1(int(input("Enter the value of N:")))   

#==================================OUTPUT======================================

""" 
Enter the value of N:10
1 8 27 64 125 216 343 512 729 1000 
 """