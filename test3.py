import sys
import random
list = ['r', 'o', 'u', 'n', 'd'];
n = 0
while n<25: 
	command = input("Enter 'a' to shuffle list:")
	if command=='a':
		random.shuffle(list)
		print ("Reshuffled list : ", list)
		n += 1
	else:
		print("You entered an incorrect command")
		command
print ("You have reached the limit of shuffling the list")
input("Press Enter to exit:")
sys.exit()
