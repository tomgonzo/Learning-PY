#Gonzo Facts - Challenge 3 and Challenge 4

gonzo = {
		"name":"Gonzo",
		"height":"182cm",
		"fav_color":"Verde"
}

response = raw_input("What do you want to know?")
if response in gonzo:
	result = gonzo[response]
	print(result)
else:
	print("I don't know that.")
