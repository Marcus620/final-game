names = {
'jaden' : "I am awesome",
'marcus' : "I have a slow car",
'jesse' : "I like eating jaden's snacks",
'michael' : "I can easily build and take apart computers"
}
print("Jaden's Code!:")
name = input("Enter name:" )
if name in names.keys():
    print("My name is", name, "and", names[name])
else:
    print("Sorry I dont know you :/")
ignore = input("")
 
print("Part 2: Jesse!")

jadeisland = 'restaraunt'

should_continue = True
while should_continue:
	task = input("Is Jade-Island a restaraunt or an island?")
	if task == 'restaraunt':
		print("You are indeed correct! There is one in New York!")
		should_continue = False
	elif task == 'island':
		print("You know, I would like to believe that jade-island is a real island, but when you refer to the island, we mean jade-marcus' small cluster of tables in Swett's class")
		should_continue = False
	elif task == 'both':
		print("You know I guess it is both a restaraunt and an island")
		should_continue = False
	else:
		continue
ignore1 = input("")

print("Marcus' Code!:")
import random
while True:
    word = input("What word do you want to meme? Type 'cancel' to stop the code: ").lower()

    if word == 'cancel':
        break
    else:
        y = []
        for i in word:
            num = random.randint(0,1)
            if num == 0:
                y.append(i.swapcase())
            else:
                y.append(i)
        word = ''
        for i in y:
            word = word + str(i)
        print(word)

part("Part 4: Michael!")
