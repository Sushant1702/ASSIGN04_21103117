#QUESTION 1

print('Answer 1')
def TowerOfHanoi(j , from_rod, to_rod, middle_rod):
	if j == 0:
		return
	
	TowerOfHanoi(j-1, from_rod, middle_rod, to_rod)
	print("Move disk",j,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(j-1, middle_rod, to_rod, from_rod)

j = 3
TowerOfHanoi(j, 'A', 'C', 'B')

#Question 2

print("Answer 2")
from math import factorial, remainder
from tracemalloc import start
n=int(input("Enter the size of pascal's triangle- "))

print("By using for loop:")

for k in range(n):
	for l in range(n-k+1):
		print(end=" ") #for spacing

	for l in range(k+1):
		print(factorial(k)//(factorial(l)*factorial(k-l)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("By using while loop:")

k=0
while(k<n):
    z=n-k+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<k+1):
        print(factorial(k) // (factorial(y) * factorial(k - y)), end=" ")
        y+=1
    k+=1
    print()
print("\n\n")

print("By using recursions:")

def pascals_triangle(n,originalength=n):
    if n == 0:
        return
    pascals_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for k in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - k) // k
    print()
pascals_triangle(n)
print("\n")


#Question 3

print("Answer 3")
i1, i2 = map(int,input("Enter two integers: ").split())                                                                  #Taking two integers
Que = i1 // i2
Rem = i1 % i2

#part a)
print('a')
print(callable(Quotient))                                                                                                #Checking whether values is a callable value or not
print(callable(Remainder))

#part b)
if (Que == 0):
    print("b) The quotient is zero.")
if (Rem == 0):
    print("b) The reminder is zero.")
if (Que != 0 and Rem != 0):
    print("b) All the values are non zero.")

#part c)
List = [Que + 4, Rem + 4, Rem + 5, Que + 5, Rem + 5, Que + 6, Rem + 6]

result = []
for i in range(len(List)):
    if List[i] > 4:
        result.append(List[i])
print(f"c) Filtered out values that are greater than 4 are: {result}")

#part d)
setresult = set(result)
print("d) Set:",setresult)

#part e)
immutableSet = frozenset(setresult)
print("e) Immutable set:",immutableSet)

#part f)
print("f) Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

#Question 4
print("Answer 4 ")
class student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):                      #Destroying Object
        print("Object destroyed.")

                                            #creating object
student1 = student("Manraj Singh Chadha", 21103115)
print("Object created.")
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")

del student1                                #deleting object

#Question 5

print("Answer 5")
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

employee1 = employee("Mehak", 40000)                                                              #Creating the employee record
employee2 = employee("Ashok", 50000)
employee3 = employee("Viren", 60000)

                                                                                                  #Updating salary
employee1.salary = 70000
print(f"a) Updated salary of {employee1.name} is {employee1.salary} ")                            #Deleting record

print("b) Record of Viren has been deleted", end='')
del employee3



#QUESTION 6

print("Answer 6")
firstword = input("Enter a word: ")                                                                #Taking a word from thr first friend
firstword = firstword.lower()


secondword = input("Enter a new meaningful word using the same letters to test your friendship: ") #Taking a meaningful word with the same letters
secondword = secondword.lower()

def count_in_dict(firstword):
    count = {}
    List = list(firstword)
    
    j = len(List)
    for i in range(j):
        if List[i] in count:
            count[List[i]] += 1
        else:
            count[List[i]] = 1
    return count

def userinput():                                                                                   #Input of the shopkeeper to verify the word
    if count_in_dict(firstword) != count_in_dict(secondword):
        print("The letters are not exact, \nFriendship is Fake.")
        return
    ask = input("Does the word makes sense? (Y or N )")

    if ask=='Y':
        print("The Friends passed the friendship test, \nFriendship is True.")
    elif ask=='N':
        print("The word doesn't have a meaning, \nFriendship is fake")
    else:
        print("Invalid input, try again with Y or N. ")
        userinput()
userinput()