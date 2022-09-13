""" 
6. Write a recursive python function to print first N even natural numbers in reverse
order.
 """
def fun1(n):
    if n>0: 
        if n%2==0:
            print(n,end=' ')
        fun1(n-1)    
       
fun1(int(input("Enter the value of N:"))*2)   

#==================================OUTPUT===================================
""" 
Enter the value of N:20
40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2
 """