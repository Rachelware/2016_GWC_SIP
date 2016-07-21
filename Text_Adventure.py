print("""You wake up one morning and find that you aren\'t in your bed; you aren\'t even in your room.
You\'re in the middle of a giant maze.
A sign is hanging from the ivy: 'You have one hour. Don\'t touch the walls.'
There is a hallway to your right and to your left.""")
first = False
while first!= True:
	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()
	if user_input == "left":
		print("You decide to go left and reach a four-way split in the path.")
		print("Type 'left' to go left, 'right' to go right, and 'forward' to go forward.\n ")
		first = True
		user_input = input()
		second = False
		while second!= True:
			if user_input == "left":
				print("You turn left and find a wall a couple feet ahead.")
				print("Type 'turn' to try another route or 'forward' to touch the wall.\n ")
				second = True
				user_input = input()
				third = False
				while third!= True:
					if user_input == "turn":
						print("you go back to the intersection. You can go 'left' or 'forward', neither path you have tread before.\n ")
						third = True
						user_input = input()
						fourth = False
						while fourth!=True:
							if user_input == "left":
								print("you go left, the maze surrounds you.")
								print("Another four-way. You decide going back is useless.\nYou have three choices, 'left', 'right', 'forward'.\n ")
								fourth = True
								user_input = input()
								fifth = False
								while fifth!= True:
									if user_input == "left":
										print("You go left. The maze continues.\nYou see a tree branch leaning into the maze.\nYou can either 'grab' or 'continue' around the corner.\n ")
										fifth = True
										user_input = input()
										sixth = False
										while sixth== False:
											if user_input == "grab":
												print("You jump and grab the branch. It is strong enough to hold you.\nStruggling, you climb onto the branch.\nThe tree conveniently is outside of the maze, and you are now in a field.\nNow you just have to find your way home.")
												sixth = True
											elif user_input == "continue":
												print("You turn right with the maze.\nAhead is a tree lined pathway.\nYou go down it and at the end have a choice between a 'shrinking potion' and a 'growing potion'.\n ")
												sixth = True
												user_input = input()
												seventh = False
												while seventh== False:
													if user_input == "shrinking potion":
														print("You shrink really small, and notice a mousehole ahead.\nYou have to run with all your strength so you can reach it in time.\nYou made it out!")
														seventh = True
													elif user_input == "growing potion":
														print("It wasn't a growing potion.\nYou find yourself unable to move. Is this the end?")
														seventh = True
													else:
														print("Input 'shrinking potion' or 'growing potion'")
														seventh = False
														user_input = input()
											else:
												print("Input 'grab' or 'continue'. ")
												user_input = input()
									elif user_input == "right":
										print("You turn right and continue on your way.\nAt the next intersection there is a metal hallway extending to your left.\nYou decide to take it.")
										print("You continue down the hallway for a while.")
										print("At the end of the long hallway are two doors:\nOne red, one blue.")
										print("Choose 'red' or 'blue'.\n ")
										fifth = True
										user_input = input()
										eighth = False
										while eighth!= True:
											if user_input == "red":
												print("The door opens into your bedroom.\nYou turn back after stepping inside, but the door has vanished.")
												eighth = True
											elif user_input == "blue":
												print("You open the door, and a torrent of water rushes out.\nOnce the room is largely dry, you try the red door.\nThe door won't budge no matter how hard you pull.\nYou are stuck in the maze.")
												eighth = True
											else:
												eighth = False
												print("Enter 'red' or 'blue'")
												user_input = input()
									elif user_input == "forward":
										print("The maze narrows slowly as you move forward unil there is barely room to keep from touching the walls.\nThere is hardly anytime left in the hour when you realize you can\'t make it this way.\nYou can 'give up' or 'go back'\n ")
										fifth = True
										user_input = input()
										ninth = False
										while ninth!= True:
											if user_input == "give up":
												print("You give up.")
												ninth = True
											elif user_input == "go back":
												print("You shimmy, then run back as fast as humanly possible.\nIt is not, however, fast enough to make up gor yur choices.\nYou don't make it out of the maze.")
												ninth = True
											else:
												print("Input 'give up' or 'go back'.\n ")
												user_input = input()
									else:
										print("Input 'left' 'right' or 'forward'.\n ")
										user_input = input()
							elif user_input == "forward":
								print("You continue forward until you reach a wall, with two choices:\n'right' or 'left'\n ")
								fourth = True
								user_input = input()
								tenth = False
								while tenth == False:
									if user_input== "right":
										print("The ivy covered maze walls give way to metal walls and you continue down the hallway for a while.")
										print("At the end of the long hallway are two doors:\nOne red, one blue.")
										print("Choose 'red' or 'blue'\n ")
										tenth = True
										user_input = input()
										eleventh = False
										while eleventh ==False:
											if user_input == "red":
												print("The door opens into your bedroom.\nYou turn back after stepping inside, but the door has vanished.")
												eleventh = True
											elif user_input == "blue":
												print("You open the door, and a torrent of water rushes out.\nOnce the room is largely dry, you try the red door.\nThe door won't budge no matter how hard you pull.\nYou are stuck in the maze.")
												eleventh = True
											else:
												print("Input 'red' or 'blue'.\n ")
												user_input = input()
												eleventh = False
									elif user_input == "left":
										print("You fall into quicksand\nThe end.")
										tenth = True
									else:
										print("Input 'left' or 'right'.")
										tenth = False
										user_input = input()
							else:
								print("Input 'left' or 'forward'\n ")
								user_input = input()
					elif user_input == "forward":
						print("You touch the wall.\nYour body feels heavy, and everything fades to darkness.\nYou have died in the maze.")
						third = True
					else: 
						print("Input 'forward' or 'turn'\n ")
						user_input = input()
			elif user_input == "back":
				print("This wasn't a choice???")
				print("Try again")
				second = False
			elif user_input == "forward":
				print("You fall into quicksand.\nYou didn't make it out of the maze.")
				second = True
			elif user_input == "right":
				print("You turn right to more of the maze ahead.")
				print("You continue forward until you reach a wall, with two choices:\n'right' or 'left'\n ")
				second = True
				user_input = input()
				twentyfour = False
				while twentyfour == False:
					if user_input == "right":
						print("You see a door ahead, with a riddle:\n'You will always find me in the past. I can be created in the present, But the future can never taint me. What am I?'")
						twentyfour = True
						user_input = input()
						twentyfive = False
						while twentyfive == False:
							if user_input == "history" or "History":
								print("Congrats! You are correct, and the door opens into your bedroom.\nWhen you look back behind you, the door is gone.")
								twentyfive = True
							else:
								print("wrong answer. You are trapped in the maze.")
								user_input = input()
					elif user_input== "left":
						print("You fall into quicksand.\nYou do not make it out of the maze.")
			else:
				print("Input 'forward' 'right' or 'left'\n ")
				user_input = input()
	elif user_input == "forward":
		print("You go forward. The maze surrounds you.")
		print("Another four-way. You decide going back is useless.\nYou have three choices, 'left', 'right', 'forward'.\n ")
		second = True
		user_input = input()
		thirteenth = False
		while thirteenth == False:
			if user_input == "left":
				print("You go left. The maze continues.\nYou see a tree branch leaning into the maze.\nYou can either 'grab' or 'continue' around the corner.\n ")
				thirteenth = True
				user_input = input()
				fourteenth = False
				while fourteenth == False:
					if user_input == "grab":
						print("You jump and grab the branch. It is strong enough to hold you.\nStruggling, you climb onto the branch.\nThe tree conveniently is outside of the maze, and you are now in a field.\nNow you just have to find your way home.")
						fourteenth = True
					elif user_input == "continue":
						print("You turn right with the maze.\nAhead is a tree lined pathway.\nYou go down it and at the end have a choice between a 'shrinking potion' and a 'growing potion'.\n ")
						fourteenth = True
						user_input = input()
						fifteenth = False
						while fifteenth == False:
							if user_input == "shrinking potion":
								print("You shrink really small, and notice a mousehole ahead.\nYou have to run with all your strength so you can reach it in time.\nYou made it out!")
								fifteetn = True
							elif user_input == "growing potion":
								print("It wasn't a growing potion.\nYou find yourself unable to move. Is this the end?")
								fifteenth = True
							else:
								print("Input 'shrinking potion' or 'growing potion'.\n ")
								fifteenth = False
								user_input = input()
					else:
						print("Input 'grab' or 'continue'\n ")
						fourteenth = False
						user_input = input()
			elif user_input == "right":
				print("You reach a three-way split. Choose 'right' or 'left'.\n ")
				thirteenth = True
				user_input = input()
				sixteenth = False
				while sixteenth== False:
					if user_input == "right":
						print("You turn right and continue on your way.\nAt the next intersection there is a metal hallway extending to your left.\nYou decide to take it.")
						print("You continue down the hallway for a while.")
						print("At the end of the long hallway are two doors:\nOne red, one blue.")
						print("Choose 'red' or 'blue'\n ")
						sixteenth = True
						user_input = input()
						twentysix = False
						while twentysix == False:
							if user_input == "red":
								print("The door opens into your bedroom.\nYou turn back after stepping inside, but the door has vanished.")
								twenysix = True
							elif user_input == "blue":
								print("You open the door, and a torrent of water rushes out.\nOnce the room is largely dry, you try the red door.\nThe door won't budge no matter how hard you pull.\nYou are stuck in the maze.")
								twentysix = True
							else:
								print("Input 'red' or 'blue'.\n ")
								twentysix = False
								user_input = input()
					elif user_input == "forward":
						print("The maze narrows slowly as you move forward unil there is barely room to keep from touching the walls.\nThere is hardly anytime left in the hour when you realize you can\'t make it this way.\nYou can 'give up' or 'go back'.\n ")
						sixteenth = True
						user_input = input()
						seventeenth = False
						while seventeenth == False:
							if user_input == "give up":
								print("You give up.")
								seventeenth = True
							elif user_input == "go back":
								print("You shimmy, then run back as fast as humanly possible.\nIt is not, however, fast enough to make up for your choices.\nYou don't make it out of the maze.")
								seventeenth = True
							else:
								print("Input 'give up' or 'go back'.\n ")
								seventeenth = False
								user_input = input()
					else:
						print("Input 'left' 'right' or 'forward'.\n ")
						thirteenth = False
						user_input = input()
			else:
				print("input 'left' 'right' or 'forward'")
				user_input = input()
	elif user_input == "right":
		print("You choose to go right and walk until you reach a split in the path\nYou can go 'left' or 'forward'.\n ")
		first = True
		user_input = input()
		eighteenth = False
		while eighteenth == False:
			if user_input == "left":
				print("You go into the new hallway, which has a hanging garden instead of roof.\nIt is pleasant, until you notice the man eating plants eyeing you.\nYou can 'fight' or 'run'.\n ")
				eighteenth = True
				user_input = input()
				ninteenth = False
				while ninteenth == False:
					if user_input == "fight":
						print("You find a plank of wood propped against the wall and swing it at the plants.\n You hit a couple, but the third breaks the plank.\nYou have to run away.\nYou don't have enough time to make it out of the maze.")
						ninteenth = True
					elif user_input == "run":
						print("You run as fast as you can through the hall, swerving and ducking.\nYou reach the end to find yourself in an atrium with birds everywhere.\nYou can 'continue' or 'take a break'.\n ")
						ninteenth = True
						user_input = input()
						twentith = False
						while twentith == False:
							if user_input == "continue":
								print("You walk through the atrium, with the time limit in mind.\nThe next room is all closed up except for a whole in the wall.\nA message underneath requests that you enter something into the hole.\nYou choose between your 'hand' and 'foot'.\n ")
								twentith = True
								user_input = input()
								twentyone = False
								while twentyone == False:
									if user_input == "hand":
										print("You reach your hand in and find a switch\nYou pull it, and a wall lifts up, revealing an escape right into your bedroom.\nOnce inside, you turn around, but it is just your normal room.")
										twentyone = True
									elif user_input == "foot":
										print("You reach your foot in, but nothing happens.\nYou can't figure out thhe room, and walk around hitting the wall.\nNothing happens.\nYou don't make it out of the maze.")
										twentyone = True
									else:
										print("Input 'hand' or 'foot'\n ")
										twentyone = False
										user_input = input()
							elif user_input == "take a break":
								print("You sit down, taking in the birds chirping and the calm.\nUnfortunately, you only had an hour, and you take too long.\nAll exits are now closed to you.")
								twentith = True
							else:
								print("Input 'continue' or 'take a break'\n ")
								twentith = False
								user_input = input()
					else:
						print("Input 'fight' or 'run'.\n ")
						user_input = input()
			elif user_input == "forward":
				print("You go forward and continue left around the corner.\nThe path continues straight for quite a while, until you see a door that says 'Staff Only'.\nIn your pocket is a key.\nYou can 'try key' or 'try doorknob'.\n ")
				eighteenth = True
				user_input = input()
				twentytwo = False
				while twentytwo == False:
					if user_input == "try key":
						print("The key doesn\'t work.\nThe knob doesn\'t work.\nThe hallway is closed behind you.\nYou don\'t make it out of the maze.")
						twentytwo = True
					elif user_input == "try doorknob":
						print("You turn the knob, and the door opens.\nYou go through the door and end up outside.\nYou recognise where you are, and start home.")
						twentytwo = True
					else:
						print("Input 'try key' or 'try doorknob'.\n ")
						user_input = input()
			else:
				print("Input 'left' or 'forward'.\n ")
				eighteenth = False
				user_input = input()
	else: 
		print("Input 'left' or 'right'")
		user_input = input()
print("Game Over. Did you make it out alive?")
