""" 
3. Write a recursive python function to print first N odd natural numbers
 """
def fun1(n):
    if n>0: 
        fun1(n-1)
        if n%2!=0:
            print(n)
       
fun1(int(input("Enter the value of N:"))*2)   

#===============================OUTPUT================================
""" 
Enter the value of N:30
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
 """
