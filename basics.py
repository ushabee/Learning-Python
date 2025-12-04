'''#print("hi")
import pyjokes
jokes= pyjokes.get_jokes()
print(jokes)'''
'''a=34
..........
b=80
if(a>b):
    print("a is greater")
else:
    print("b is greater") 
 
       '''
#remainder
"""a =  int (input ("enter the number:" ))
z= int (input("enter value of z : "))
k = a % z
print("remainder is ",k)"""
#to print the average of the two numbe
#rs 

'''a= int(input("enter 1st number"))
b= int (input("enter 2nd num"))
c = (a + b)/2
print("avg is ",c)'''
# to print the square of number
'''a= int(input("enter the number"))
sqare= a**2
print("square of the num is ",sqare)'''
#to print user input name with attached good 
'''a = str(input("write the name")) #a= input("enter the name")
print("Good Afternoon",a)'''# print(f("good afternoon{a}")) f= formatted string 
# to print the given letter template
'''Letter = """ Dear <|name|>,
you are selected! 
<|date|>
"""
print(Letter.replace("<|name|>","coco").replace("<|date|>", "5th september 2025"))
'''
#to find the double space 
'''name= "hi,Iam good"
print(name.find("  ")) ''' #find() method also helps to give the index e.g ....find("goo")
'''a = "Iam good"
print(a.replace("","  "))'''
#lists and tuples
'''l1= [3,6,7,4]
#l1.sort()
l1.reverse()
print(l1)
'''
#to print the fruits name entered by the user 

''' fruits = []
for i in range(5):
 p = input ("enter the name of the fruit: ")
 fruits.append(p) 
print(fruits)'''
# to ask the name of 6 students and display them in sorted form 
'''students = []
for i in range(5):
 k = input("enter the name of the student : ")
 students.append(k)
 students.sort()
print(students)'''
#to sum a list with 4 numbers
'''list = [1,3,4,6]
p=0
for x in list : 
    p+=x
print(p)
list=[1,2,3,4]
print(sum(list))'''
#to count the number of 1s in the tuple
'''a=(3,1,4,5,1,3)
print (a.count(1))'''
#to create a dict of hindi words with values as their eng translation within  option  to look it up 
'''dict = {
    "billu":"cat",
    "ladki": "gurl",
    "ladka":"boy"
}
a = input("enter the word u want: ")
print(dict[a])'''
#wap to input eight numbers from the user and display all unique numbers once 
'''s= set()
p = input("enter a number:")
s.add(int (p))
p = input("enter a number:")
s.add(int(p))
p = input("enter a number:")
s.add(int(p))
p = input("enter a number:")
s.add(int(p))
p = input("enter a number:")
s.add(int(p))
print(s)'''
#using loop 
'''s = set()
for x in range(5):
    n = input("enter the num :")
    s.add(int(n))
print (s)   
'''
#checking if we can have same thing as string and int in the set 
'''s = set()
s.add(18)
s.add("18")
print(s)'''
# 1==1.0 #python automatically converts int to float before the comparision so it's true 
'''s= set()
s.add(1)
s.add(1.0)
s.add("1")
print(len(s))  #ans is 2 
s={}
print(type(s))'''# dict
# creating an empty dict and allowing 4 users to enter their fav languages using their names as key 
'''d = {}
for i in range(4):
    key= input("enter your name: ")
    value = input("enter ur favourite language: ")
    d[key]= value
print(d)'''
# can we change the value inside a list which is inside sets
'''s =(8,4,5,[1,2])
print(s) # we can't since lists aren't hashable ''' # tuples are hashable, int and strings are but not dict and lists and sets
#print (hash(10))
#to find the greatest of four numbers entered by the user
'''n= int(input("enter the number: "))
m = int(input("enter the 2nd num:"))
o = int(input("enter the 3rd num :"))
p = int(input("enter the 4th num :"))
greatest = n
if( m> greatest):
    greatest = m
if(o> greatest):
    greatest =o
else :
    greatest = p
print("the greatest num is :",greatest)'''
#to find whether the student passed or failed if it requires a totla of 40 % and atleast 33% in each subject to pass.
'''a = int(input("enter the marks in eng:"))
b= int(input("enter the marks in maths:"))
c= int(input("enter the marks in sci:"))
d = ((a+b+c)/300)*100
if(a>33 and b>33 and c>33 and d>=40):
    print("pass")
else:
    print("fail")'''
# to detect the given spams 
''''a="make a lot of money"
b="buy now"
c= "subscribe this"
d= "click this"
i = input("enter your comment: ")
if (a in i or b in i or c  in i):
    print("the message is spam")
else:
  print("the message is not a spam")'''

#to find whether a given username contains less than 10 characters or not 
'''b = input("enter the your name :")
c= len(b)
if(c<10):
    print("yes it has less than 10 char")
else:
    print("no it has more ")
'''
#to find out if given name is present in a list or not 
'''d = ["ana","Anne","John","Harry"]
c =  input("enter a name :")
if(c in d ):
    print("yes the name is in the list")
else:
    print("no the name isn't in the list")'''
#loops
#to print multipliacation table of given number using for loop 
'''n = int (input("enter a number:"))
for i in range(1,11):
 j = i*n
 print ( f"{n} * {i} = {j}")'''
# to great the person names that starts with 'S' in a list
'''L= ["harry","Sonam","Sachin","Rahul"]
for i in L:
    if (i.startswith("S")):
        print("hey",i)
'''
# multiplication with while loop 
'''n = int(input("enter the number:"))
i=1
while(i<11):
    j = n*i
    print(f"{n}*{i}={j}")
    i+=1
'''
#to  check if the num is the prime number or not 
'''n = int(input("enter the number:"))
c=0
for i in range(1,n+1):
    if(n % i==0):
        c=c+1
if(c==2):
    print("it's prime")
else:
    print("it's composite")'''
#to find the sum of the first n natural numbers using while loop 
'''n = int(input("enter the number:"))
sum = 0
i=0
while(i<n+1):
    sum = sum + i
    i+=1
print(sum)
'''
#to calculate the factorial of a number using for loop 
'''n = int (input("enter a number:"))
fact =1
for i in range(1,n+1):
    fact = fact *i
print(f"factorial of {n}  is {fact}")'''
# to print the star pattern:  for n =3
'''n= int(input("enter value:4"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end=" ")
    print()
#and
n= int(input("enter value:4"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i,end=" ")
    print()'''
#and
'''n= int(input("enter value:"))
for i in range(1,n+1):
    if(i==1 or i==n):
     print("*"*n)
    else:
      print("*" ,end= "")
      print(" "*(n-2),end="")
      print("*" ,end= "")
    print()'''

#multiplication table in reverse orderr
'''n = int (input("enter a number:"))
for i in range(1,11):
 print ( f"{n} * {11-i} = {(11-i)*n}")
'''
'''## function calling and testing 
def goodday(name, ending):
    print("Good Day"+ name)
    print(ending)
    return"ok"
a= goodday("harry","thankyou")
print(a) '''
#recursion
'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n= int(input("enter a number:"))
print(f"factorial of the number is {fact(n)}")
    '''
#use function to find the greatest of 3 numbers
'''def great():
    n1=int(input("enter a number:"))
    n2=int(input("enter 2nd num:"))
    n3=int(input("enter the 3rd num:"))
    greatest=n1
    if(n2>greatest):
        greatest=n2
    if(n3>greatest):
        greatest=n3
    print("greatest number is",greatest)
great()'''
'''def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=5
b=3
c=2
print(f"the greatest num is,{great(a,b,c)}")'''

#to convert celsius to fahrenheit

'''''def CtoF(C):
 C = float(input("enter the value in celsius:"))
 return (9/5)*C+32
 print(f"value in fahrenheit is ,{CtoF(C)"})
CtoF()'''''
# using recursive to print the sum of first n natural numbers

'''def sum(n):
 if n==1:
    return 1
 else:
   return n+sum(n-1)
n=int(input("enter a number:"))
print("sum to the number is:",sum(n))'''
# function to print first "n" lines of following pattern 
'''pattern
* * *
* *
* '''
'''def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)
n= int(input("enter the value of n:"))
pattern(n)'''
#function that converts inches to cms
'''def in_cm():
    i=float(input("enter the value of inch:"))
    cm= 2.54*i
    print(f"value in cm is {cm}")
in_cm()'''
# to remove a given word froma list and strip it at the same time 
'''def rem(l,word):
    word = word.strip()   # clean any spaces
    if word in l:
        l.remove(word)
    return l
l = ["Ana", "Anne", "Mack", "an"]
print(rem(l, "an"))'''
# to remove the number 
'''def list():
    L=[1,2,1,2,4]
    K=[]
    for i in L:
        if i in K:
            continue
        else:
            K.append(i)
    print(K)       
list()'''    
    

    
       

    




