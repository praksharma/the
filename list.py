#BOOK WORK


#LIST OPERATION..
#1print a normal list in animal while/for loop.
'''animals=['zebra','tiger','lion','jackal','kangaroo']
using while loop
i=0
while i<len(animals):
    print(animals[i])
    i+=1
for a in animals:
    print(a)'''

#2.usnig enumerate(indexing with one by one print) function.
'''animals=['zebra','tiger','lion','jackal','kangaroo']
for index, a in enumerate(animals):
    print(index,a)'''

#3.mutable list(mutable means change for ex:insert modified remove etc).
'''animals=['zebra','tiger','lion','jackal','kangaroo']
ages=[25,26,25,27,26,28,25]
animals[2]03 3eee4ee='rhinoceros'
ages[5]=31
ages[2:5]=[24,25,32]
ages[2:5]=[]'''

#4.concatenation(means add a value at the end in list).
'''lst=[12,13,14,15,16]
lst=lst+[33,44,56]
print(lst)'''

#5.merging(means 2 list ko merge[2 list ko ek krna]krna phir usse new list create hota hai).
'''s=[200,300,400]
t=[23,34,78]
z=s+t
print(z)'''

#6.conversion(mtlb converted:string ke data ko list me convert krna list function ka use krke).
'''i=list('africa')  #string ek data type hota hai jisme text ko store and process krne ki suvidha deta hai(character,text).
print(i)'''

#7.aliasing(means ek list ko 2 naamo se bulana mtlb 1 list ko  2 naam se bulana pr list 1 hi ho.iska mtlb jb hum pehle list me koi changes krti hu to dusre me bhi changes hoga mtlb equal honge dono).
'''lst1=[20,30,40,50]
lst2=lst1
print(lst1)
print(lst2)
lst1[0]=100
print(lst1[0],lst2[0])'''

#8.cloning(ka mtlb hota hai copy krna first ko same as copy krna dusre me.lekin agar hm first list me changes krte hai to second me koi update nhi hota wo as a tis rhega.
'''lst1=[10,20,30,40,50]
lst2=[]
lst2=lst2+lst1
print(lst1)
print(lst2)
lst1[0]=100
print(lst1[0],lst2[0])'''

#9.searching(using a 'in & not in' membership operator usig a searchig list).
'''lst=['a','e','i','o','u']
res='a' in list
res='z' not in list'''

#10.identity(identity mtlb check krna .agar 2 value same hai to true pr agar alag alag hai to false.
'''lst1=[10,20,30,40,50]
lst2=[10,20,30,40,50]
lst3=lst1
print(lst1 is lst2)   #false
print(lst1 is lst3)   #true
print(lst1 is not lst2)  #true'''

#11.note the diff for basic types like int/str.
'''num1=10       #int
num2=10
s1='hi'     #str
s2='hello'
  print(num1 is num2)  #same value define(a=12,b=12) means true: but diff value(a=12,b=14) define means false
print(s1 is s2)'''

#12.comparison(means compare krna 2 list ke bich me.
'''a=[1,2,3,4]
b=[23,34,2]
print(a<b)'''

#13.emptyness we can check if a list s empty using not operator.
'''lst=[]
if in lst:
print('empty lst')'''

#14.deleted operation.
'''lst=[21,23,12,34,45,34]
del lst[3]    #means remove a 3rd item in a list.
del lst[2,5]   #means remove a 2nd& 5th item in a list.
del lst[:]     #delete entire list
lst[]          #another way  to delete a entire list'''


#15.multible variable are provide same list but agar a variable ko delete krte hai to ek hi delete hoga na ki sb.
'''lst1=[2,3,4,5,6,7,8]
lst3=lst2=lst1
lst1=[]
lst2[:]=[]   #list is empty deleting all items
print(lst2)
print(lst3)'''

#16  nested list
'''a=[1,3,5,7,9]
b=[2,4,6,8,10]
c=[a,b]
print(c[0][0],c[1][2])'''

# 17 list added another list
'''x=[1,2,4,6,9,8]
y=[10,20,30,x,80]
print(y)'''

#18. str & list within a list using a * operatr.
'''s='hello'
i=[*s]
print(i)'''





























