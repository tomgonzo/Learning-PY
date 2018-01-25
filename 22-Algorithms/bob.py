#Bottles of beer!

def bottles_of_beer(bob):
	if bob < 1:
		print("No more bottles of beer on the wall. :(")
		return

	tmp = bob
	bob -= 1
	print(f"""{tmp} bottles of beer on the wall. 
		{tmp} bottles of beer. Take one down, 
		pass it around, {bob} bottles of beer on the wall.""")

	bottles_of_beer(bob)

bottles = input("How many bottles of beer on the wall? ")
bottles = int(bottles)
bottles_of_beer(bottles)