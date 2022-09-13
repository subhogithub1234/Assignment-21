""" 
4. Write a recursive python function to print first N odd natural numbers in reverse order
 """

def fun1(n):
    if n>0: 
        if n%2!=0:
            print(n,end=' ')
        fun1(n-1)    
       
fun1(int(input("Enter the value of N:"))*2)   

#===============================OUTPUT=========================================
""" 
Enter the value of N:20
39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1 
 """