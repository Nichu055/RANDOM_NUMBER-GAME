import random
print('welcome to the game of guess what is the number, Do you think you smarter then the computer then play on')
category = input("""
    choose your difficulty
    select 1,2 or 3 (Type digits only)
    1 => Beginner
    2 => Intermediate
    3 => Pro
	\n""")
if category == "1":
	rand_num = random.randrange(1,5)
	guess = int(input("Guess a number between 1 to 5 - \n"))
	if rand_num == guess:
		print(f"""
			Computer number was : {rand_num}
			You guessed : {guess}
			Congratulation!!! You beat the computer
			""")
	else:
		while guess != rand_num:
			print(f"""
				computer number is :{rand_num}
				you guessed:{guess}
				try again""")
			rand_num = random.randrange(1,5)
			guess = int(input("Guess a number between 1 to 5 - \n"))
			if guess == rand_num:
				print(f"""
					computer number was :{rand_num}
					you guessed:{guess}
					ha ha you won""")
elif category == "2":
	rand_num = random.randrange(1,10)
	guess = int(input("Guess a number between 1 to 10 - \n"))
	if rand_num == guess:
		print(f"""
			Computer number was : {rand_num}
			You guessed : {guess}
			Congratulation!!! You beat the computer
			""")
	else:
		while guess != rand_num:
			print(f"""
				computer number is :{rand_num}
				you guessed:{guess}
				try again""")
			rand_num = random.randrange(1,10)
			guess = int(input("Guess a number between 1 to 10 - \n"))
			if guess == rand_num:
				print(f"""
					computer number was :{rand_num}
					you guessed:{guess}
					ha ha you won""")
	
elif category == "3":
	rand_num = random.randrange(1,15)
	guess = int(input("Guess a number between 1 to 15 - \n"))
	if rand_num == guess:
		print(f"""
			Computer number was : {rand_num}
			You guessed : {guess}
			Congratulation!!! You beat the computer
			""")
	else:
		while guess != rand_num:
			print(f"""
				computer number is :{rand_num}
				you guessed:{guess}
				try again""")
			rand_num = random.randrange(1,15)
			guess = int(input("Guess a number between 1 to 15 - \n"))
			if guess == rand_num:
				print(f"""
					computer number was :{rand_num}
					you guessed:{guess}
					ha ha you won""")
else:
	print("Incorrect input")
input()
