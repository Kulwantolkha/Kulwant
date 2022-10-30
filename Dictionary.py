# Dictionary is nothing but key value pairs
x={}
print(type(x))
y={"Rahul":"Infosys","Ankit":"Tata","Vikram":"Wipro","Ajay":"TCS"}
print(y)
#We can add dictionary in dictionary also Eg.
z={"Mobile":{"Android":"Samsung","IOS":"Apple"},"Stationary":{"Notebook":"Classmate","Pen":"Pentonic"}}
print(z)
#To print a outcome of a single name given use the below type
print(y["Vikram"])
#To add one more item in dictionary
y["Rajesh"] = "Hitachi"
print(y)
#To delete a item from a dictionary
del y["Rajesh"]
print(y)
#To print a item from a dictornary in a dictionary
print(z["Stationary"])
#Similar to line number 10
print(y.get("Rahul"))
#To add(similar to line number 11)
y.update({"Rakesh":"Redmi"})
print(y)
#To print keys in means first outcome in a dictionary
print(y.keys())
print(z.keys())
print(y.items())
print(z.items())