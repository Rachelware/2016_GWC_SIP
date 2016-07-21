import random 

five_syllables = ["At the silent pond", "Keeping in the dark", "Hold on to the sound", "Waves roll over sand", "Keeping memories", "Never give it up", "Time to worry not", "The leaves turn light green","With time comes beauty","And silence returns", "Staring at the sun","It's now or never ","Where do you belong","Nothing stays the same"]
seven_syllables = ["The light dances through shadow", "Small movement brings large effects", "Whistling wind changes appearance", "The water stiffles the sound","The strength of the salks shows through","A gentle breeze allows calm","Hopeful branches reach skyward","An open feeling beginning","Careful movements in the wind","Rain falls disparately now"]

five_syllables_length = len(five_syllables)
seven_syllables_length = len(seven_syllables)

print("Generated Haikus:")
print( )

for i in range(3):
	random_index = random.randint(0, five_syllables_length-1)
	print(five_syllables[random_index])
	stuff = five_syllables[random_index]
			
	random_index2 = random.randint(0, seven_syllables_length-1)
	print(seven_syllables[random_index2])
	stuff2 = seven_syllables[random_index2]

	three = False
	while three == False:
		random_index = random.randint(0, five_syllables_length-1)
		if five_syllables[random_index] == stuff:
			three = False
		else:
			print(five_syllables[random_index])
			three = True
			stuff3 = five_syllables[random_index]

	print()
	