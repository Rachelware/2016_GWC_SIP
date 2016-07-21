import random 

five_syllables = ["At the silent pond", "Keeping in the dark", "Hold on to the sound", "Waves roll over sand", "Keeping memories", "Never give it up", "Time to worry not", "The leaves turn light green","With time comes beauty","And silence returns", "Staring at the sun","It's now or never ","Where do you belong","Nothing stays the same"]
seven_syllables = ["The light dances through shadow", "Small movement brings large effects", "Whistling wind changes appearance", "The water stiffles the sound","The strength of the salks shows through","A gentle breeze allows  calm","Hopeful branches reach skyward","An open feeling beginning","Careful movements in the wind","Rain falls disparately now"]

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
	

		
one = False
while one == False:
	random_index = random.randint(0, five_syllables_length-1)
	if five_syllables[random_index] == stuff or stuff3:
		one = False
	else:
		print(five_syllables[random_index])
		one = True
		stuff4 = five_syllables[random_index]
		
		
two = False
while two== False:
	random_index2 = random.randint(0, seven_syllables_length-1)
	if seven_syllables[random_index2] == stuff2:
		two =False
	else:
		print(seven_syllables[random_index2])
		stuff5 = seven_syllables[random_index2]
		one = True

four = False
while four == False:
	random_index = random.randint(0, five_syllables_length-1)
	if five_syllables[random_index] == stuff or stuff3 or stuff4:
		four = False
	else:
		print(five_syllables[random_index])
		stuff6 = five_syllables[random_index]
		four = True

print( )
	
	
five = False
while five == False:
	random_index = random.randint(0, five_syllables_length-1)
	if five_syllables[random_index] == stuff or stuff3 or stuff4 or stuff6:
		five = False
	else:
		print(five_syllables[random_index])
		stuff7 = five_syllables[random_index]
		five = True
	
two = False
while two== False:
	random_index2 = random.randint(0, seven_syllables_length-1)
	if seven_syllables[random_index8] == stuff2 or stuff5:
		two =False
	else:
		print(seven_syllables[random_index2])
		stuff8 = seven_syllables[random_index2]
		one = True

four = False
while four == False:
	random_index = random.randint(0, five_syllables_length-1)
	if five_syllables[random_index] == stuff or stuff3 or stuff4 or stuff6 or stuff7:
		four = False
	else:
		print(five_syllables[random_index])
		stuff9 = five_syllables[random_index]
		four = True
	
print( )
done()	
	
	
	
	
	
	
	
	
	
	