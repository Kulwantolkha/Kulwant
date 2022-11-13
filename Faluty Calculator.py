
# #Faulty calculator
# print("please choose your operation from the list,provide the number only for 1 to 4 "
#       "\n1 for Addition "
#       "\n2 for subtraction "
#       "\n3 for multiplication "
#       "\n4 for division ")
# N=input()


# if N=="1":
#     print("you chose addition")
# elif N=="2":
#     print("you chose substration")
# elif N=="3":
#     print('you chose multiplication')
# else :
#     print("you chose division")
# print('enter frist number')
# a=int(input())
# print("enter secind no.")
# b=int(input())

# if N=="1":

#     if a==56 or 9 and b==9 or 56:
#         print('77 is your answer')
#     else :
#         print( int(a) +int(b)," is your answer")



# # if N=="2":
# #     print(int(a)-int(b),"is your answer")

# # if N=="3":
# #     if a==45 or 3 and b==3 or 45:
# #         print("555 is your answer")
# #     else:
# #         print('int(a)*int(b)',"is your answer")

# # if N=="4":
# #     if a==56 or 6 and b==6 or 56:
# #         print('4 is your answer')
# #     else:
# #         print(int(a)//int(b),"is your answer")

# # exit()

# print("enter the first number")
# n1 = int(input())
# print("enter the second number")
# n2 = int(input())
# if n1 == 45 and n2 == 3:
#     print("the multiple is ",555)
# if n1 == 56 and n2 == 9:
#     print("the sum is", 77)
# if n1 == 56 and n2 == 6:
#     print("the division is ",4)
# else:
#     print("the sum of the numbers is",int(n1)+int(n2))
#     print("the multiple is ",int(n1)*int(n2))
#     print("the division is",int(n1)/int(n2))
#     print("the subtraction is",int(n1)-int(n2))


#Faulty Calculator
print("What do you want to do?\nAddition(+)\nSubstraction(-)\nMultiplication(*)\nDivision(\)")
a= input()
print("Enter your first number.")
b=int(input())
print("Enter your second number.")
c=int(input())
if a=="+":
    if b==56 and c==56 or c==65 and b==65 or b==16 and c==5:
        print("90 is your required answer")
    else:
        print(int(b)+int(c),"is your required answer")

if a=="-":
    if b==45 and c ==45 :
        print("11 is your answer")
    else:
        print(int(b)-int(c),"is your required answer")

if a=="*":
    if b==90 and c == 9:
        print("1 is your required answer")
    else:
        print(int(b)*int(c),"is your required answer")

if a=="/":
    if b==55 and c==5 :
        print("I is your answer")
    else:
        print(int(b)//int(c),"is you required answer")

print("Thanks!")
