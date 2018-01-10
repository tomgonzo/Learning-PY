#Dictionary of Favorite Tracks - Challenge 5

tracks = {
	"Infected Mushroom":"Becoming Insane",
	"Pink Floyd":"Comfortably Numb",
	"ACDC":"Thunderstruck"
}

question = raw_input("Give me an artist name:")
if question in tracks:
	print("Listen to"), tracks[question], ("by them!")
else:
	print("Haven't heard of them! I'll check them out!")