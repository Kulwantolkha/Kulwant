#This system of function is used to print separetly all the items of a list,sets,toople . Here lets we have 100 items in list so in order to print these item in new line:
#for loop is use to enter in the list to get search for individual items of the list.
x =  ["Photo","Gallery","Clip","Video","Camera","Area"]
for item in x:
    print(item)

#For list in list form:
#How to unpack list:

y=[["Photo",2], ["Gallery",4],["Clip",6],["Video",8],["Camera",10],["Area",12]]

for item,number in y:
    print(item,"has",number,"items.")

#to print these in dictionary style
z= dict(y)
# for item, number in y:
print(z)
#After making it dictionary you can print only items of that dictionary of that dictionary :
for item in z:
    print(item)



