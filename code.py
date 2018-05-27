names = {
'jaden' : "Is awesome",
'marcus' : "I have a slow car",
'jesse' : "I like eating jaden's snacks",
'michael' : "I can burp"
}
name = input("Enter name:" )
if name in names.keys():
    print("My name is", name, "and", names[name])
else:
    print("Sorry I dont know you :/")
 
print("hey")
