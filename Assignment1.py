#use of different operators
a=33
b=54
####################     Arithmatic Operators     #################
sum=a+b
print(sum)

sub=a-b
print(sub)

pro=a*b
print(pro)

div=a/b
print(div)

sq=a**2
print(sq)

c=a//2
print(c)

###################       Assignment Operators    ################
x=8
y=5
x+=2
print(x)

y-=3
print(y)

x*=5
print(x)
y/=2  
print(y)

##################      Comparision Operators      ################
w=a<b
print(w)
u=x==y
print(u)
x<=a
y>=b


#################        Logical operators        ################
g=a==b and x>=y
print(g)
a>x and b>=y
h=a==b or x>=y
print(h)

###############         Membership Operators      #################
a=[1,22,45,10]
t=3 in a
print(t)




#********************    Algorithm     ************************
step 1: start
step 2:a=10
step 3:b=1
step 4:a-2
step 5:b+2

#Assignment 1.2

#logical operators in If-else
x=2
y=5
if x==2 and x<y:
  print("here both condition are satisfied ")
 
if x>=y or y==8:
  print("Here either or both condition are satisfied ")


#Calculator

print("***************** Calculator *********************")
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
print("       1.For addition")
print("       2.For substraction")
print("       3.For product")
print("       4.For division")


val=int(input("Enter the number of method you want to perform : "))
if val==1:
   sum=a+b
   print("The sum of two numbers is : ",sum)
elif val==2:
    sub=a-b
    print("The differencs of two numbers is : ",sub)
elif val==3:
    pro=a*b
    print("The product of two numbers is : ",pro)
elif val==4:
    di=a/b
    print("The division of two numbers gives : ",di)
else:
   print("invalid choice ")

