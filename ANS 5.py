""" 
5. Write a recursive python function to print first N even natural numbers.
 """
def fun1(n):
    if n>0: 
        fun1(n-1)
        if n%2==0:
            print(n,end=" ")
       
fun1(int(input("Enter the value of N:"))*2) 

#==================================OUTPUT====================================
""" 
Enter the value of N:40
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42
 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80
 """