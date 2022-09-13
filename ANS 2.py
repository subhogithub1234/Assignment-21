""" 
2. Write a recursive python function to print first N natural numbers in reverse order
 """
def fun1(n):
    if n>0:
       print(n,end=" ")
       n=fun1(n-1)
fun1(int(input("Enter the value of N:")))       

#========================================OUTPUT===================================
""" 
Enter the value of N:10
10 9 8 7 6 5 4 3 2 1 
 """