 # 1.print a row &column program.

'''for i in range(0,5):    #row
    for j in range(0,5): #column
        print(j,end=" ")
    print()'''

'''for i in range(0,10):
    print(i,end=" ")
for i in range(0,10):
    print(i)'''


# 2.write a program to create a calculator.
'''a=int(input("enter first value"))
b=int(input("enter second value"))
x=0
while x<5:
    print('1.add')
    print('2.substract')
    print('3.multiply')
    print('4.division')
    print('5.exit')
    x=int(input("enter your choice"))
    if x==1:
        c=a+b
        print('sum:',c)
    elif x==2:
        c=a-b
        print('difference:',c)
    elif x == 3:
         c = a * b
         print('product:', c)
    elif x==4:
        c=a/b
        print('quotient:',c)
    elif x==5:
        break
print()'''

 # 3.write a program to remove a duplicate element for a list.
'''k=[2,3,4,5,66,78,67,66,57,68,78,1,2,3,4,2,3,2]
k2=[]
for i in k:
    if(i not in k2):
        k2.append(i)
print(k2)'''

'''import numpy
k=[2,3,4,5,66,78,67,66,57,3,4,2]
k=numpy.array(k)
k2=numpy.unique(k)
print(k2)'''


# 4.write a program to create a hotel order for a customer.

'''total=0
while True:
    print("1.cold drink")
    print("2.snacks")
    print("3.dinner")
    print("4.exit")
    x=int(input("enter the choice"))
    if(x==1):
        while True:
            print("1.pepsi-20")
            print("2.dew-30")
            print("3.exit")
            n=int(input("enter the choice"))
            if(n==1):
                n2=int(input("enter the quantity"))
                total=total+n2*20
                print(total)
            elif(n==2):
                n2=int(input("enter the quantity"))
                total=total+n2*30
                print(total)
            elif(n==3):
                break
    elif(x==2):
        while True:
            print("1.samosa-20")
            print("2.burger-30")
            print("3.exit")
            n=int(input("enter the choice"))
            if(n==1):
                n2=int(input("enter the quantity"))
                total=total+n2*20
                print(total)
            elif(n==2):
                n2=int(input("enter the quantity"))
                total=total+n2*30
                print(total)
            elif(n==3):
                break
    elif(x==4):
      break

print(total)'''



#5. write a program to create a data for 5 student marks percentage and total defined.
'''names=['reena','seema','madhu','ram','rajesh']
subjects=['math','english','hindi','science','history']
reena=[]
seema=[]
madhu=[]
ram=[]
rajesh=[]
for subject in subjects:
   mark=float(input("enter "+subject+" subject mark for " + names[0]))
   reena.append(mark)
print(reena)
per=(sum(reena)/500)*100
print("percentage is",per)
if per<=70:
   print('fail')
else:
   print('pass')

for subject in subjects:
   mark=float(input("enter "+subject+" subject mark for " + names[1]))
   seema.append(mark)
print(seema)
per=(sum(seema)/500)*100
print("percentage is",per)
if per<=70:
   print('fail')
else:
   print('pass')

for subject in subjects:
   mark=float(input("enter "+subject+" subject mark for " + names[2]))
   madhu.append(mark)
print(madhu)
per=(sum(madhu)/500)*100
print("percentage is",per)
if per<=70:
   print('fail')
else:
   print('pass')


for subject in subjects:
   mark=float(input("enter "+subject+" subject mark for " + names[3]))
   ram.append(mark)
print(ram)
per=(sum(ram)/500)*100
print("percentage is",per)
if per<=70:
   print('fail')
else:
   print('pass')


for subject in subjects:
   mark=float(input("enter "+subject+" subject mark for " + names[4]))
   rajesh.append(mark)
print(rajesh)
per=(sum(rajesh)/500)*100
print("percentage is",per)
if per<=70:
   print('fail')
else:
   print('pass')'''


# 6.write a program to print any no. of table while loop..
'''n=int(input("enter the value="))
x=1
while(x<11):
    print(n*x)
    x = x +1
    
# 7.write a program to print any no. of table for loop.

n=int(input("enter the value="))
x=1
for i in range(0,10):
    print(n*x)
    x = x+1'''

# 8.write a program to print a any no. of  factorial.
'''n=int(input("enter number to find a factorial="))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(f"factorial of {n} ={fact}")'''


#9.write a program to create a 5 table.
'''n=5
for i in range(1,11):
    print(n, "x",i,"=",n*i)'''

#10..write a program to create a calculator condition as if else.

'''def calculator():
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice = input("enter choice(1/2/3/4):")
if choice in('1','2','3','4'):
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
if choice == '1':
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif choice == '2':
    result = num1 - num2
    print(f"{num1}-{num2}={result}")
elif choice == '3':
    result = num1 * num2
    print(f"{num1}*{num2}={result}")
elif choice == '4':
    result = num1 / num2
    print(f"{num1}/{num2}={result}")'''


#11..write a program to create a calculator.
'''a=int(input("enter first value"))
b=int(input("enter second value"))
x=0
while x<5:
    print('1.add')
    print('2.substract')
    print('3.multiply')
    print('4.division')
    print('5.exit')
    x=int(input("enter your choice"))
    if x==1:
        c=a+b
        print('sum:',c)
    elif x==2:
        c=a-b
        print('difference:',c)
    elif x == 3:
         c = a * b
         print('product:', c)
    elif x==4:
        c=a/b
        print('quotient:',c)
    elif x==5:
        break
print()'''

 # 12..write a program to remove a duplicate element for a list.
'''k=[2,3,4,5,66,78,67,66,57,68,78,1,2,3,4,2,3,2]
k2=[]
for i in k:
    if(i not in k2):
        k2.append(i)
print(k2)'''

'''import numpy
k=[2,3,4,5,66,78,67,66,57,3,4,2]
k=numpy.array(k)
k2=numpy.unique(k)
print(k2)'''

#13..write a program to print any no. of table while loop..
'''n=int(input("enter the value="))
x=1
while(x<11):
    print(n*x)
    x = x +1'''

# 14..write a program to print any no. of table for loop.

'''n=int(input("enter the value="))
x=1
for i in range(0,10):
    print(n*x)
    x = x+1'''

# 15..write a program to print a any no. of  factorial.
'''n=int(input("enter number to find a factorial="))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(f"factorial of {n} ={fact}")'''


#16..write a program to create a calculator for "if else" condition.

def calculator():
    print("simple calculator")
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    choice=input("enter the choice(1/2/3/4):")
    num1=float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    if choice=='1':
        result=num1+num2
        print("f{num1}+{num2}={result}")
        elif choice=='2':
        result = num1 - num2
        print("f{num1}-{num2}={result}")
        elif choice == '3':
        result = num1 * num2
        print("f{num1}*{num2}={result}")
        elif choice == '4':
        result = num1 / num2
        print("f{num1}/{num2}={result}")
    else:
        print("can not divide by zero")
    else:
    print("invalid input.please enter a valid choice.")


#17










