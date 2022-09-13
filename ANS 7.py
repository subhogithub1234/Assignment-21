""" 
7. Write a recursive python function to print squares of first N natural numbers
 """
def fun1(n):
    if n>0:

       fun1(n-1) 
       print(n**2,end=" ")
      
fun1(int(input("Enter the value of N:")))       

#========================================OUTPUT===============================
""" 
Enter the value of N:10
1 4 9 16 25 36 49 64 81 100
 """
