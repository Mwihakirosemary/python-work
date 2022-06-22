#coplex
from re import M


x = 9 + 8j
y = 10 + 4.5j
z = 11.2 + 1.2j
print(type(x))

print(x)
print(y)
print(z)

#casting a float value to an integer
pi = 3.14
print(type(pi))

num = int(pi)
print("Integer number:", num)
print(type(num))

#casting a boolean to an integer
flag_true = True
flag_false = False
print(type(flag_true))

num1 = int(flag_true)
num2 = int(flag_false)
print("Integer number 1:", num1)
print(type(num1))

print("Integer number 2:", num2)
print(type(num2))

#casting a string to an integer
sting_num = "125"
print(type(sting_num))
nim1 = int(sting_num)
print("Integer number 1:", nim1)
print(type(nim1))

# if statements
number = 6
if number > 5:
    print(number * number)
print('Next lines of code')

#if else statement
password = input("Enter password ")
if password == "1mind&boby":
    print("Corrrect password")
else:
    print("Incorrect password")

#chain multiple if statement
def user_check(choose):
    if choose == 1:
        print("Admin")
    elif choose == 2:
        print("Editor")
    elif choose == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)

#Nested if-else:
numb1 = int(input("Enter first number "))
numb2 = int(input("Enter second number "))
if numb1 >= numb2:
    if numb1 == numb2:
        print(numb1,'and',numb2,'are equal')
    else:
        print(numb1,'is greater than',numb2)
else:
    print(numb1,'is smaller than',numb2)

#Single statement suites
number = 23
if number > 0: print("Positive")
else: print("Negative")

x = 5
while x <= 10: print(x,end=" "); x = x+1

#for loop - used to iterate over a sequence such as a list,string,tuple &/range are executed a fixed number of times
# While loops execute until the condition is true

for i in range(10):
    print(i)
# range(how many times the code block will be executed)
#print sum of all even numbers
sum = 0     #set a var to 0
for x in range(2,22,2):    #use a for loop to iterate over the range where (from 2,to 20 the nums div by 2)
    sum = sum + x        #add the current number to the sum variable
print(sum)

numbers = [2,3,4,5,6]
for n in numbers:    #iterate over elements in list numbers
    square = n **2   # use the ** exponent arithmetic operator
    print('The square of:',n,'is:',square) 
#calculate the average of a list of numbers
numb = [10,20,30,40,50]
sum = 0
for w in numb:  # definate iteration - runs code 5 time bcs it contains 5 elemen
    sum = sum + w
    list_size = len(numb)
    average = sum / list_size
print(average)
#print all even and odd numbers
for z in range(1,11):
    if z % 2 == 0:
        print("This is an even number", z)
    else:
        print("This is an odd number", z)
#use for loop to generate a list of numbers from 9 to 50 divisible by 2
for s in range(10,52,2):
        print(s)
#Break statement used to terminate a loop
#break the loop if the number is greater than 15
sums = [12,10,5,7,20,23,30]
for y in sums:
    if y > 15:
        break
    else:
        print(y)
#continue statement skips the current iteration of a loop and jumps into the next iteration
#count the total number of 'm' in a given string
name = "miriam mendoza"
count = 0
for char in name:
    if char != 'm':
        continue
    else:
        count = count + 1 
print("Tatal number of m is",count)   
#else block - print done after the iteration
for f in range(1,7):
    print(f)
else:
    print("done")
# else with break statement
cont = 0
for p in range(1,6):
    cont = cont + 1
    if cont > 2:
        break
    else:
        print(p)
else:
    print('Done')
#Backward iteration using reversed()
list1 = [10,20,30,40,50]
for i in reversed(list1):
    print(i)
#Backward iteration using range()
num = 5
for num in (range(5,-1,-1)):
    print(num)
#reverse using a loop
numbers = [1,2,3,4]
for n in numbers[::-1]:
    print(n)
#Nested for loops - for loop inside another for loop
#used with 2 dimensional arrays
#nested for loop to print a pattern
rows = 5
for i in range(1,rows + 1): # Outer loop is the number of rows to print
    for j in range(1,i + 1): # Inner loop is the number of columns - columns count get increamented by 1
        print('*',end=" ")
    print('')

#While loop is an entry controlled loop & for loop is a count controlled loop
#print the multiplication table of hte first 5 numbers using for loop and a while loop
for u in range(1,6):
    print('Multiplication table of', u)
    count = 1
    while count < 11:
        print(u * count, end='')
        count = count + 1
    print('\n')
#print the even numbers by adding 1 to the odd numbers in the list
odd = [1,3,5,7,9]
even = [i + 1 for i in odd if i % 2 == 1]
print(even)
#Enumerate - accessing both the value & its index number
names = ["Rose","Mary","Mwihaki"]
for x,v in enumerate(names):
    print('names[',x,']=',v)
#printing elements in a lits with their index using range
numbs = [1,5,6,7,8]
numbs_length = len(numbs)
for n in range(numbs_length):
    print('index:',n,'value',numbs[n])
#iterate a string usig a for loop
nam ="Mwihaki"
for m in nam:
    print(m,end=' ')
#iterate a string in reverse order
nam ="Mwihaki"
for m in nam[::-1]:
    print(m,end=' ')
#iterate over a particular set of char in a string
nam ="Mwihaki"
for m in nam[2:3:5]:
    print(m,end=' ')

