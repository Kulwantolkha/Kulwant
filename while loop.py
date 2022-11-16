# *** It is very important to see that if x is putted over while loop and x=x+1 is given in last then only it will add the given value in it 
# #for loop runs till the list or the given items does not end but on the otherhand while loop runs till the condition valid or continue
# #if we write i=0 on the top  and use 'while' module then print(i) then endless 0 will be printed but if we print(i+1) then 0+1=1 will be printed endlessly but if we put the required output in the end like here it will be 1,2,3.... 
i=0
while(i<45):
    print(i)
#here i is 0 so 0 will alwalys remain less than 0
#so it will never discontinue it will always be in running stage
    i=i+1
#so here we gave a suitable condition to it this miss end somewhere
#if we want to print form 1 
print(i+1)
#to get in straight line
print(i, end='')


#take input from the user until the user give you input greater than 100
while(True):
    x=int(input("Enter a number="))
    if x>100:
        print("Congratulation")
        break
    else:
        print("Try again")
        continue
#here we can see that x is below while so while loop is applicable on x that's why if we give a input other if and else input are applied on it then again while loop does it's work and ask for a input


#take input from the user until the user give you input greater than 100
x=int(input("Enter a number="))
while(True):
    if x>100:
        print("Congratulation")
        break
    else:
        print("Try again")
        continue
#Here in this we can see that x is above while loop it means that wile loop is not applicable on x if a number greater than 100 given as input then it will print that number infinite time 


