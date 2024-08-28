#check even/odd function
def check_Even_Odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
#square of a num function
def square(num):
    return pow(num, 2)

#prime number function
def isPrime(num):
    for i in range(2, num//2):
        if num%i!=0:
            continue
        else:
            return False
    return True

name:str
num:str
numList:list=[]
name=input("Enter your name: ")
for i in range(3):
    num=input(f"Enter a number {i+1}: ")
    numList.append(int(num))
print(f"Hi, {name}, welcome to Python Learning!!..")
even_odd_tuple_list = []
for num in numList:
    even_odd_tuple_list.append((num, check_Even_Odd(num)))
print(even_odd_tuple_list)
num_square_tuple_list=[]
for num, str in even_odd_tuple_list:
    num_square_tuple_list.append((num, square(num)))
sum:int=0
for num, square in num_square_tuple_list:
    print(f"The number {num} and its square: ({num}, {square})")
    sum+=int(num)
print(f"Amazing! The sum of your favorite numbers is: {sum}")
if isPrime(sum):
    print(f"Wow, {sum} is a prime number!")
else:
    print(f"Number {sum} is not a prime number!")