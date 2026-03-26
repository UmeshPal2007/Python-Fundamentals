#First Program
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
marks = float(input("Enter Your Marks : "))

print("Your Name is : ", name)
print("Your Age is : ", age)
print("Your Marks are : ", marks)

#Write a Program to input user's First Name & Print its Length.

name= str(input("Enter Your First Name : "))
print("Length Of your name : ", len(name))

#Write a Program to find the occurence of "$" in a String.

str = "If I spend $10 on lunch, $5 on coffee, $20 on gas, $15 on snacks, and $50 on a new shirt, I will have spent a total of $100 today."
print("Total Number of Count : ",(str.count("$")))


#write a program to check if a nunber entrered by the user is odd or even.

num = int(input("Enter a number : "))
if (num % 2 == 0):
    print("Number is : Even")
else:
    print("Number is Odd")

#write a program to find the Greatest of 3 numbers entered by the user.

a= int(input("Enter First Number : "))
b= int(input("Enter Second Number : "))
c= int(input("Enter Third Number : "))
if(a >= b and a >= c):
    print("First Number Is Grestest : " , a)
elif(b >= c):
    print(("Second Number Is Grestest : " , b))
else:
    print(("Third Number Is Grestest : " , c))